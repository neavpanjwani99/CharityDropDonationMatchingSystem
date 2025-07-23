
from flask import Flask, Response, render_template, request, redirect, flash, url_for, session
from flask import send_file
from datetime import datetime
import io
import csv
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import re
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

@app.route('/')
def home():
    return render_template('home.html')

#@app.route('/donate')
#def donate():
#    return render_template('donate.html')

#  Donation Form Submission
@app.route('/donate', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        form = request.form

        first_name = form.get('first_name')
        last_name = form.get('last_name')
        email = form.get('email')
        phone = form.get('phone')
        donation_type = form.get('donation_type')
        food_option = form.get('food_option')
        study_items = ', '.join(request.form.getlist('study_items'))
        cash_purpose = form.get('cash_purpose')
        message = form.get('message')
        amount = 100.00  # Replace with dynamic if needed

        user_id = session.get('user_id', None)

        cursor = mysql.connection.cursor()
        cursor.execute("""
            INSERT INTO donations (user_id, first_name, last_name, email, phone, donation_type, 
                                   food_option, study_items, cash_purpose, message, amount)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (user_id, first_name, last_name, email, phone, donation_type, 
              food_option, study_items, cash_purpose, message, amount))
        mysql.connection.commit()
        cursor.close()

        # 3. Redirect to thank you page with details
        full_name = f"{first_name} {last_name}"
        return redirect(
            f"/thankyou?fullName={full_name}&email={email}&phone={phone}"
            f"&course={donation_type}&total={amount}&paid={amount}"
        )

    return render_template('donate.html')



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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact_faq.html')

@app.route('/impact')
def impact():
    return render_template('impact.html')

@app.route('/admin/starter')
def admin_starter():
    return render_template('admin_starter.html')

@app.route('/admin/dashboard')
def admin_dashboard():  
    # is me se session hata diya hai (insert it (If logedin then only admin open ho ese route karke na ho open (for all)))
    stats = [
        {"title": "Total Donation", "value": "₹15,000"},
        {"title": "Total Donors", "value": "45"},
        {"title": "Transactions", "value": "50"},
        {"title": "Avg Donation", "value": "₹333"},
    ]
    donors = [
        {"name": "Ravi", "email": "ravi@example.com", "amount": 1000, "date": "2025-07-20", "status": "Success"},
    ]
    latest_donations = [
        {"name": "Asha", "email": "asha@example.com", "amount": 1500, "date": "2025-07-21", "method": "UPI"},
        {"name": "Raju", "email": "raju@example.com", "amount": 2000, "date": "2025-07-19", "method": "Card"},
    ]
    chart_labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    chart_data = [500, 1000, 750, 1200, 1800, 1600]

    return render_template("admin_home.html",
        admin_name="Neav",
        stats=stats,
        donors=donors,
        latest_donations=latest_donations,
        chart_labels=chart_labels,
        chart_data=chart_data
    )

@app.route('/add-cause', methods=['GET', 'POST'])
def add_cause():
    if not session.get('admin_logged_in'):
        flash("You must be logged in as admin to access this page.", "warning")
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        # Save to DB logic placeholder
        flash('✅ New cause added successfully!', 'success')
        return redirect(url_for('admin_dashboard'))

    return render_template('addcauses.html')

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
