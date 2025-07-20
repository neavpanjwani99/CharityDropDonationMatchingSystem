from flask import Flask, render_template, request, redirect, flash, url_for
from datetime import datetime
import re

app = Flask(__name__)
app.secret_key = 'giveSyncSuperSecretKey'  # Required for flashing messages

# Home
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
        email = request.form['email']
        password = request.form['password']

        # Dummy login logic (replace with DB check)
        if email == 'admin@example.com' and password == 'admin123':
            return redirect('/')
        else:
            flash('Invalid credentials, please try again.', 'danger')
            return render_template('login.html')

    return render_template('login.html')

# Register Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('pass')
        confirm = request.form.get('cpass')

        # Basic email format validation
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
