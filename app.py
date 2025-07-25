
from flask import Flask, Response, render_template, request, redirect, flash, url_for, session
from flask import send_file
from datetime import datetime
import random
import io
import csv
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import re
from flask_mail import Mail, Message    # For contact form email
import geocoder
import requests     # For geolocation (if needed, but not used in this code)

app = Flask(__name__)
app.secret_key = 'giveSyncSuperSecretKey'

# MySQL Config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'charitydrop'

mysql = MySQL(app)


# ---------- MAIL CONFIG ----------
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'charitydropa@gmail.com'
app.config['MAIL_PASSWORD'] = 'zema qqmt yqar uobb'  # NOT Gmail password. Use App Password
app.config['MAIL_DEFAULT_SENDER'] = 'charitydropa@gmail.com'

mail = Mail(app)

# ---------- ROUTES ----------
@app.route('/')
def home():
    return render_template('home.html')

#@app.route('/donate')
#def donate():
#    return render_template('donate.html')

#  Donation Form Submission
from flask import jsonify, request, redirect, render_template, session

@app.route('/donate', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        form = request.form

        # Basic fields
        first_name = form.get('first_name')
        last_name = form.get('last_name')
        email = form.get('email')
        phone = form.get('phone')
        donation_type = form.get('donation_type')  # Selected from dropdown
        food_option = form.get('food_option')      # Only if type is food
        study_items = ', '.join(form.getlist('study_items'))  # List to string
        cash_purpose = form.get('cash_purpose')
        message = form.get('message')

        # 🟡 Dynamic amount: check cash or food amount
        cash_amount_raw = form.get('cashAmount') or form.get('foodAmount')
        try:
            amount = float(cash_amount_raw) if cash_amount_raw else 0.0
        except ValueError:
            amount = 0.0

        # Validate amount for cash
        if donation_type == 'cash' and amount <= 0:
            return jsonify({"error": "Please enter a valid cash amount."}), 400

        # Logged-in user ID
        user_id = session.get('user_id', None)

        try:
            cursor = mysql.connection.cursor()
            cursor.execute("""
                INSERT INTO donations (
                    user_id, first_name, last_name, email, phone, donation_type, 
                    food_option, study_items, cash_purpose, message, amount
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                user_id, first_name, last_name, email, phone, donation_type,
                food_option, study_items, cash_purpose, message, amount
            ))
            mysql.connection.commit()
            cursor.close()
        except Exception as e:
            print("DB Error:", e)
            return jsonify({"error": "Database error occurred."}), 500

        # Thank you redirect
        full_name = f"{first_name} {last_name}"
        redirect_url = f"/thankyou?fullName={full_name}&email={email}&phone={phone}&course={donation_type}&total={amount}&paid={amount}"
        return jsonify({"redirect": redirect_url})

    else:
        # 🟡 GET method: fetch donation types from DB for dropdown
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT name FROM donation_types")
        types = cursor.fetchall()
        donation_types = [t[0] for t in types]
        cursor.close()

        return render_template('donate.html', donation_types=donation_types)






@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()

        if user:
            db_password = user[2]
            role = user[10]

            if check_password_hash(db_password, password):
                session['user_id'] = user[0]
                session['email'] = user[1]
                session['role'] = role

                # ✅ Get public IP
                try:
                    ip = requests.get('https://api64.ipify.org?format=json').json()['ip']
                except Exception:
                    ip = 'Unknown'

                # ✅ Get location from public IP
                g = geocoder.ip(ip)
                city = g.city if g.ok else 'Unknown'
                country = g.country if g.ok else 'Unknown'
                now = datetime.now()

                # ✅ Save login log with geolocation
                cursor.execute("""
                    INSERT INTO login_logs (user_id, ip_address, city, country, login_time, role)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (user[0], ip, city, country, now, role))
                mysql.connection.commit()
                cursor.close()

                if role == 'admin':
                    session['admin_logged_in'] = True
                    flash("✅ Admin login successful!", "success")
                    return redirect('/admin/dashboard')
                else:
                    flash("✅ User login successful!", "success")
                    return redirect('/')
            else:
                flash("❌ Incorrect password.", "danger")
        else:
            flash("❌ Email not found.", "danger")

    return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('pass')
        confirm = request.form.get('cpass')
        twitter = request.form.get('twitter')
        facebook = request.form.get('facebook')
        gplus = request.form.get('gplus')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        phone = request.form.get('phone')
        address = request.form.get('address')

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            flash("Invalid email format.", "danger")
            return render_template("register.html")



        if password != confirm:
            flash("Passwords do not match.", "danger")
            return render_template("register.html")

        hashed_password = generate_password_hash(password)
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("""
                INSERT INTO users (email, password, twitter, facebook, gplus, fname, lname, phone, address)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (email, hashed_password, twitter, facebook, gplus, fname, lname, phone, address))
            mysql.connection.commit()
            cursor.close()
            flash("✅ Registration successful!", "success")
            return redirect(url_for("login"))
        except Exception as e:
            flash(f"❌ Error: {str(e)}", "danger")
            return render_template("register.html")



    return render_template("register.html")


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html',
        fullName=request.args.get('fullName', 'Donor'),
        phone=request.args.get('phone', ''),
        email=request.args.get('email', ''),
        course=request.args.get('course', 'Donation'),
        total=request.args.get('total', ''),
        paid=request.args.get('paid', ''),
        date=datetime.now().strftime("%d-%m-%Y")
    )

#@app.route('/contact', methods=['GET', 'POST'])
#def contact():
 #   return render_template('contact_faq.html')

 # ---------- CONTACT ROUTE ----------
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        user_id = session.get('user_id')  # if user is logged in

        if not all([name, email, subject, message]):
            flash("All fields are required.", "danger")
            return redirect('/contact')

        # INSERT into MySQL
        cursor = mysql.connection.cursor()
        cursor.execute("""
            INSERT INTO contact_messages (user_id, name, email, subject, message)
            VALUES (%s, %s, %s, %s, %s)
        """, (user_id, name, email, subject, message))
        mysql.connection.commit()
        cursor.close()

        # SEND EMAIL to Admin
        try:
            msg = Message(
                subject=f"[Contact Form] {subject}",
                recipients=['charitydropa@gmail.com'],
                body=f"""
                        📬 New Contact Message

                        From: {name}
                        Email: {email}
                        User ID: {user_id or 'Guest'}

                        Subject: {subject}

                        Message:
                            {message}
                                    """
            )
            mail.send(msg)
        except Exception as e:
            print("Mail send error:", e)
            flash("❌ Something went wrong. Please try again later.", "danger")
            return redirect('/contact')


    return render_template('contact_faq.html')


@app.route('/impact')
def impact():
    return render_template('impact.html')

@app.route('/admin/starter')
def admin_starter():
    return render_template('admin_starter.html')

@app.route('/admin/dashboard')
def admin_dashboard():
    if 'admin_logged_in' not in session:
        flash("Access denied! Please log in as admin.", "danger")
        return redirect(url_for('login'))

    admin_id = session.get('user_id')

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT fname FROM users WHERE id = %s AND role = 'admin'", (admin_id,))
    admin = cursor.fetchone()
    admin_name = admin[0] if admin else 'Admin'

    # ✅ Stats
    cursor.execute("SELECT COUNT(DISTINCT user_id) FROM donations")
    total_donors = cursor.fetchone()[0]

    cursor.execute("SELECT AVG(amount) FROM donations")
    avg_donation_result = cursor.fetchone()[0]
    avg_donation = f"₹{int(avg_donation_result)}" if avg_donation_result else "₹100"

    cursor.execute("SELECT SUM(amount) FROM donations")
    total_donation_result = cursor.fetchone()[0]
    total_donation = f"₹{int(total_donation_result)}" if total_donation_result else "₹0"

    cursor.execute("SELECT COUNT(*) FROM donations")
    transactions = cursor.fetchone()[0]
    cursor.close()

    stats = [
        {"title": "Total Donation", "value": total_donation},
        {"title": "Total Donors", "value": total_donors},
        {"title": "Transactions", "value": transactions},
        {"title": "Avg Donation", "value": avg_donation},
    ]

    # ✅ Pagination Logic
    page = int(request.args.get('page', 1))
    per_page = 5  # Show 5 entries per page
    offset = (page - 1) * per_page

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM donations")
    total_donor_count = cursor.fetchone()[0]
    total_pages = (total_donor_count + per_page - 1) // per_page

    # ✅ Donor list
    cursor.execute("""
        SELECT 
            CONCAT(first_name, ' ', last_name) AS name,
            email,
            amount,
            DATE(donation_time) AS date,
            donation_type
        FROM donations
        ORDER BY donation_time DESC
        LIMIT %s OFFSET %s
    """, (per_page, offset))
    donor_rows = cursor.fetchall()
    donors = []
    for row in donor_rows:
        donors.append({
            "name": row[0],
            "email": row[1],
            "amount": row[2],
            "date": row[3],
            "donation_type": row[4],
            "status": "Success"
        })

    BADGE_CLASSES = [
    "primary", "secondary", "success", "danger",
    "warning text-dark", "info text-dark", "dark"
    ]

    # ✅ Latest 4 Donations
    cursor.execute("""
    SELECT 
        CONCAT(first_name, ' ', last_name) AS name,
        email,
        amount,
        DATE(donation_time) AS date,
        donation_type
    FROM donations
    ORDER BY donation_time DESC
    LIMIT 4
    """)
    latest_rows = cursor.fetchall()
    latest_donations = []
    for row in latest_rows:
        donation_type = row[4] if row[4] else "Unknown"
        badge = random.choice(BADGE_CLASSES)  # 🎨 Random color

        latest_donations.append({
            "name": row[0],
            "email": row[1],
            "amount": row[2],
            "date": row[3],
            "type": donation_type,
            "badge_class": badge
        })


    cursor.close()

    chart_labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    chart_data = [500, 1000, 750, 1200, 1800, 1600]

    return render_template("admin_home.html",
        admin_name=admin_name,
        stats=stats,
        donors=donors,
        latest_donations=latest_donations,
        chart_labels=chart_labels,
        chart_data=chart_data,
        page=page,
        total_pages=total_pages
    )

@app.route('/add-cause', methods=['GET', 'POST'])
def add_cause():
    if not session.get('admin_logged_in'):
        flash("You must be logged in as admin to access this page.", "warning")
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form['title']
        duration = request.form['duration']
        target_amount = request.form['target_amount']
        category = request.form['category']
        other_reason = request.form.get('other_reason', None)
        description = request.form['description']
        image = request.files.get('image')

        # Determine which category to store
        donation_type_to_store = other_reason if category == 'Others' else category

        cursor = mysql.connection.cursor()

        # ✅ Check if donation_type already exists
        cursor.execute("SELECT id FROM donation_types WHERE name = %s", (donation_type_to_store,))
        existing = cursor.fetchone()

        if not existing:
            cursor.execute("INSERT INTO donation_types (name) VALUES (%s)", (donation_type_to_store,))
            mysql.connection.commit()

        # ✅ Save cause in causes table
        cursor.execute("""
            INSERT INTO causes (title, duration, target_amount, category, description)
            VALUES (%s, %s, %s, %s, %s)
        """, (title, duration, target_amount, donation_type_to_store, description))
        mysql.connection.commit()
        cursor.close()

        flash("✅ Cause added successfully!", "success")
        return redirect(url_for('admin_dashboard'))

    # GET request → fetch donation types for dropdown
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT name FROM donation_types")
    types = cursor.fetchall()
    donation_types = [{"name": t[0]} for t in types]
    cursor.close()

    return render_template('addcauses.html', donation_types=donation_types)


@app.route('/add-partner', methods=['POST', 'GET'])
def add_partner():
    if request.method == 'POST':
        name = request.form['partner_name']
        ratio = request.form['match_ratio']
        email = request.form.get('email')
        note = request.form.get('note')

        # Add to DB logic here...
        flash('Partner added successfully!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('add-partner.html')

@app.route('/download_matched_csv', methods=['GET'])
def download_matched_csv():
    data = [
        ['Donor Name', 'Partner NGO', 'Amount', 'Cause'],
        ['Neav', 'Helping Hands', '500', 'Education'],
        ['Manya', 'Relief Org', '1000', 'Food']
    ]

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerows(data)
    output.seek(0)

    return send_file(
        io.BytesIO(output.getvalue().encode()),
        mimetype='text/csv',
        as_attachment=True,
        download_name='matched_donations.csv'
    )
    
@app.route('/view_matched_donations')
def view_matched_donations():
    matched_donations = [
        {
            'donor_name': 'Neav',
            'donor_email': 'neav@gmail.com',
            'cause': 'Education',
            'amount': 500,
            'partner_name': 'Helping Hands',
            'date': datetime(2024, 7, 20)
        },
        {
            'donor_name': 'Manya',
            'donor_email': 'manya@gmail.com',
            'cause': 'Food',
            'amount': 1000,
            'partner_name': 'Relief Org',
            'date': datetime(2024, 7, 18)
        }
    ]
    return render_template('view_matched_donations.html', matched_donations=matched_donations)


if __name__ == '__main__':
    app.run(debug=True)
