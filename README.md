# 🎗️ CharityDrop — Donation & NGO Matching Platform

> 🏆 **3rd Prize Winner — Software Development Competition**

A full-stack donation platform built with Flask and MySQL that connects donors with NGOs through an intelligent donation matching system. Supports multiple donation categories including cash, food, and study materials.

---

## 🚀 Tech Stack

**Backend:** Python, Flask, Flask-MySQLdb, Flask-Mail  
**Frontend:** HTML, CSS, Jinja2 Templates  
**Database:** MySQL  
**Auth:** Werkzeug password hashing, Flask sessions  
**Other:** Geocoder (login location tracking), CSV export  

---

## ✨ Features

### 👤 Donor
- Register & login with secure Werkzeug hashed passwords
- Donate across multiple categories — **Cash, Food, Study Materials**
- Dynamic donation form based on selected category
- Receive a personalized **Thank You** page after donation
- Contact admin via built-in contact form (email notification sent)

### 🛡️ Admin
- Secure admin dashboard with role-based access
- View real-time stats: Total Donations, Total Donors, Transactions, Avg Donation
- Paginated donor list with donation history
- Add and manage **Causes** with target amounts and categories
- Add **NGO Partners** with custom match-ratio logic
- View matched donations and export them as **CSV report**
- **Login logs** with geolocation tracking (IP, city, country)

### 🤝 NGO Matching Engine
- Dynamic donation matching system with configurable match ratios
- Admin can add partners and define custom match ratios (1:1, 1:2, custom)
- `match_ratios` and `partners` tables handle flexible NGO matching

---

## 🔐 Security
- Passwords hashed using **Werkzeug** (`generate_password_hash` / `check_password_hash`)
- Role-based session management (Donor vs Admin)
- Login activity logged with **IP address, city, country, and timestamp**
- Admin routes protected with session checks

---

## 📁 Project Structure

```
CharityDropDonationMatchingSystem/
├── app.py                  # Main Flask application — all routes & logic
├── charitydrop.sql         # Full MySQL database schema + seed data
├── requirements.txt        # Python dependencies
├── static/
│   ├── assets/             # Images and logos
│   └── component/          # CSS stylesheets per page
└── templates/
    ├── home.html
    ├── donate.html
    ├── login.html
    ├── register.html
    ├── thankyou.html
    ├── impact.html
    ├── contact_faq.html
    ├── admin_home.html     # Admin dashboard
    ├── addcauses.html      # Add donation cause
    ├── add-partner.html    # Add NGO partner
    ├── view_matched_donations.html
    └── component/          # Reusable navbar & footer
```

---

## 🗄️ Database Tables

| Table | Description |
|-------|-------------|
| `users` | Donors and admins with hashed passwords and role |
| `donations` | All donation records with type, amount, and timestamp |
| `donation_types` | Dynamic categories (Cash, Food, Education, etc.) |
| `causes` | Campaigns created by admin with target amounts |
| `partners` | NGO partners linked with match ratios |
| `match_ratios` | Configurable donation match ratio values |
| `login_logs` | Login history with IP, city, country, and role |
| `contact_messages` | Messages submitted through the contact form |

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.10+
- XAMPP (MySQL + Apache) or any MySQL server

### Steps

```bash
# 1. Clone the repository
git clone <repo-url>
cd CharityDropDonationMatchingSystem

# 2. Install dependencies
pip install -r requirements.txt

# 3. Import the database
# Open phpMyAdmin → Create DB 'charitydrop' → Import charitydrop.sql

# 4. Run the app
python app.py
```

App will run at: `http://127.0.0.1:5000`

### Requirements (requirements.txt)
```
Flask
flask-mysqldb
Flask-Mail
Werkzeug
geocoder
```

---

## 📊 Key Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Home page |
| `/register` | GET/POST | Donor registration |
| `/login` | GET/POST | Login with geolocation logging |
| `/donate` | GET/POST | Multi-category donation form |
| `/thankyou` | GET | Donation confirmation page |
| `/contact` | GET/POST | Contact form with email notification |
| `/admin/dashboard` | GET | Admin panel with stats & donor list |
| `/add-cause` | GET/POST | Admin: Add donation cause/campaign |
| `/add-partner` | GET/POST | Admin: Add NGO partner with match ratio |
| `/view_matched_donations` | GET | View donor-NGO matches |
| `/download_matched_csv` | GET | Export matched donations as CSV |

---

## 🏆 Achievement

Built for and presented at a **Software Development Competition** — secured **3rd Prize** 🥉

---

## 👥 Team

Built by **BSc IT students: Manya & Neav, VESASC, Chembur, Mumbai**

---

## 📄 License

This project is for educational purposes.
