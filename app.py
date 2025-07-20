from flask import Flask, render_template, request, redirect, flash, url_for
import re

app = Flask(__name__)
app.secret_key = 'giveSyncSuperSecretKey'  # Required for flashing messages

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/donate')
def donate():
    return render_template('donate.html')

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

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('pass')
        confirm = request.form.get('cpass')

        # 🛡️ Basic email format validation
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            flash("❌ Invalid email format.", "danger")
            return render_template("register.html")

        # 🔐 Check if passwords match
        if password != confirm:
            flash("❌ Passwords do not match.", "danger")
            return render_template("register.html")

        # 💾 Future: Save to DB here
        # Example:
        # save_user_to_db(email=email, password=hash(password))

        flash("✅ Registration successful!", "success")
        return redirect(url_for("login"))

    return render_template("register.html")

if __name__ == '__main__':
    app.run(debug=True)
