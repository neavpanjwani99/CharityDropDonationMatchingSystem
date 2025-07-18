from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# Combined donation form route (GET + POST)
@app.route('/donate', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        amount = request.form.get('amount')
        cause = request.form.get('cause')
        message = request.form.get('message')

        print(f"✅ Donation received: {name} | ₹{amount} | Cause: {cause} | Email: {email}")

        # Redirect to thank you page (optional)
        return render_template('thank_you.html', name=name)

    return render_template('donate.html')

# Optional Thank You page if someone navigates directly
@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html', name="Donor")

if __name__ == '__main__':
    app.run(debug=True)
