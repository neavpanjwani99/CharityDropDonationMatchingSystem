from flask import Flask, render_template, request, redirect, flash, url_for, session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import re
from datetime import datetime


app = Flask(__name__)
app.secret_key = 'giveSyncSuperSecretKey'  # Required for flashing messages


# Home

# MySQL Config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  # blank by default in XAMPP
app.config['MYSQL_DB'] = 'charitydrop'

mysql = MySQL(app)


@app.route('/')
def home():
    return render_template('home.html')

# Donate Page
@app.route('/donate')
def donate():
    return render_template('donate.html')

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        role = request.form['role']
        email = request.form['email']
        password = request.form['password']

        # Fetch user with matching email and role
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s AND role = %s", (email, role))
        user = cursor.fetchone()
        cursor.close()

        if user:
            db_password = user[2]  # assuming password is the 3rd column (index 2)
            if check_password_hash(db_password, password):
                # ✅ Store user info in session
                session['email'] = email
                session['role'] = role

                flash("✅ Login successful!", "success")

                # Redirect based on role
                if role == 'admin':
                    return redirect('/admin/dashboard')  # Create this page separately
                else:
                    return redirect('/')
            else:
                flash("❌ Incorrect password.", "danger")
        else:
            flash("❌ Invalid email or role.", "danger")

    return render_template('login.html')


# Register Page
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


        # Basic email format validation
        # Email validation
 
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            flash(" Invalid email format.", "danger")
            return render_template("register.html")


        # Check if passwords match


        if password != confirm:
            flash(" Passwords do not match.", "danger")
            return render_template("register.html")


        # Future: Save to DB here
        # Example:
        # save_user_to_db(email=email, password=hash(password))

        flash("Registration successful!", "success")
        return redirect(url_for("login"))

        # Hash the password before storing
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
    fullName = request.args.get('fullName', 'Donor')
    phone = request.args.get('phone', '')
    email = request.args.get('email', '')
    course = request.args.get('course', 'Donation')
    total = request.args.get('total', '')
    paid = request.args.get('paid', '')
    date = datetime.now().strftime("%d-%m-%Y")

    return render_template(
        'thankyou.html',
        fullName=fullName,
        phone=phone,
        email=email,
        course=course,
        total=total,
        paid=paid,
        date=date
    )
    
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact_faq.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
