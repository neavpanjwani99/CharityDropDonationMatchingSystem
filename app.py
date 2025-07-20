from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'giveSyncSuperSecretKey'  # Required for flashing messages

# Home page
@app.route('/')
def home():
    return render_template('home.html')  # You can change to 'login.html' if needed

# Donate page
@app.route('/donate')
def donate():
    return render_template('donate.html')

# Login page (GET + POST logic)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Simple login check (replace with DB later)
        if email == 'admin@example.com' and password == 'admin123':
            return redirect('/')
        else:
            flash('Invalid credentials, please try again.', 'danger')

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)  # ✅ FIXED
