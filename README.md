## 📖 Overview

Traditional traffic violation management relies heavily on paper challans, which are prone to loss, manual errors, and slow verification. 

The **Smart Traffic Violation Logger** solves this by providing a secure, digital platform for traffic police officers to log violations and for citizens to instantly verify their fines. Officers get a powerful dashboard with real-time analytics, while citizens can simply scan a QR code on their digital receipt to view their challan status—no login required.

---

## ✨ Key Features

### 👮 For Traffic Officers (Authenticated)
- **Secure Authentication:** Officer registration and login with hashed passwords (First user automatically becomes Admin).
- **Digital Challan Generation:** Log vehicle numbers, violation types, locations, dates, and fine amounts. Unique Challan Numbers are generated automatically.
- **Records Management:** Search, filter (by vehicle, status, type, date range), and paginate through all violations.
- **Status Updates:** Mark challans as "Paid" and add a payment reference number.
- **Dashboard Analytics:** Visualize total violations, unpaid/paid counts, collected fines, and a 7-day trend chart.
- **Admin Panel:** View a list of all registered officers.
- **CSV Export:** Download all violation records for external reporting.

### 🧑‍🤝‍🧑 For Citizens (Public Access)
- **QR Code Verification:** Every challan generates a unique QR code linking to a public verification page.
- **Instant Status Check:** Citizens can verify violation details and payment status by scanning the QR or manually entering a Challan Number.
- **No Login Required:** Public pages are accessible 24/7 without authentication.

### 🎨 UI/UX Design
- **Modern Glassmorphism:** Animated navbar and gradient floating background orbs.
- **Micro-Interactions:** Staggered card animations, animated stat counters, and hover lift effects.
- **Responsive:** Fully mobile-first design using Bootstrap 5.
- **Print-Friendly:** Challans are formatted to be printed as physical receipts.

---

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| **Backend Framework** | Flask 3.0 (Application Factory, Blueprints) |
| **Database & ORM** | SQLite, SQLAlchemy |
| **Authentication** | Flask-Login, Werkzeug Security (Password Hashing) |
| **Forms & Security** | Flask-WTF, WTForms (CSRF Protection) |
| **QR Generation** | `qrcode`, `Pillow` |
| **Frontend** | Jinja2, HTML5, Bootstrap 5, Chart.js |
| **Styling** | Custom CSS3 (Glassmorphism, Keyframe Animations) |

---

## 📂 Folder Structure

```text
smart-traffic-violation-logger/
├── app/
│   ├── __init__.py          # Application Factory & Config
│   ├── models.py            # SQLAlchemy Models (Officer, Violation)
│   ├── forms.py             # WTForms & Validation
│   ├── utils.py             # QR Code generation helper
│   ├── auth/                # Authentication Blueprint
│   ├── main/                # Dashboard Blueprint
│   ├── violations/          # Challan CRUD Blueprint
│   ├── public/              # Public Verification Blueprint
│   ├── templates/           # Jinja2 HTML Templates
│   └── static/css/          # Custom CSS Animations
├── config.py                # Configuration Settings
├── run.py                   # Entry Point
├── requirements.txt         # Python Dependencies
└── .gitignore               # Files to ignore in Git
🚀 Getting Started
Follow these steps to run the project locally on your machine.

Prerequisites
Python 3.10 or higher installed

Git installed

1. Clone the Repository
bash
git clone https://github.com/YourUsername/smart-traffic-violation-logger.git
cd smart-traffic-violation-logger
2. Create and Activate a Virtual Environment
Windows:

bash
python -m venv venv
venv\Scripts\activate
macOS/Linux:

bash
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
bash
pip install -r requirements.txt
4. Run the Application
bash
python run.py
5. Open in Browser
Visit http://127.0.0.1:5000 in your web browser.

💡 First Time Setup: Since the database starts empty, click "Register" to create the first officer account. This account will automatically be granted Admin privileges.

📸 Screenshots

Dashboard	
<img width="1896" height="903" alt="Screenshot 2026-10-03 120008" src="https://github.com/user-attachments/assets/dc7f1dc0-1b31-4f94-9a4a-68450accfc76" />

Violation Records
<img width="1897" height="902" alt="Screenshot 2026-10-03 120052" src="https://github.com/user-attachments/assets/9fc903a9-dd2e-48f9-bf2a-e21d7c825dc6" />

Add Violation	
<img width="1915" height="903" alt="Screenshot 2026-10-03 120117" src="https://github.com/user-attachments/assets/df365915-0e5b-4098-8efd-4e179f9b4af9" />

Officers
<img width="1907" height="906" alt="Screenshot 2026-10-03 120213" src="https://github.com/user-attachments/assets/e784a34e-17d1-450a-b825-a1f4dab25ab9" />

QR Code Challan
<img width="1892" height="908" alt="Screenshot 2026-10-03 122458" src="https://github.com/user-attachments/assets/4175a3e9-fabe-4b86-a02f-94c9e922d97b" />

Verify Challan
<img width="1900" height="910" alt="Screenshot 2026-10-03 120232" src="https://github.com/user-attachments/assets/dfedd93c-f630-4f89-8a7c-b52d01eff0f4" />

🔐 Security Features
Password Hashing: Passwords are never stored in plain text (uses Werkzeug generate_password_hash).

CSRF Protection: All forms are protected against Cross-Site Request Forgery using Flask-WTF.

Session Management: Secure user sessions via Flask-Login.

Role-Based Access: Admin-only routes are protected from unauthorized access.

🔮 Future Enhancements
□ Integration with online payment gateways (Razorpay/Stripe).
□ SMS/Email notifications to vehicle owners.
□ Mobile application for officers (React Native/Flutter).
□ OCR integration for automatic number plate recognition.
□ Geolocation tagging of violations using GPS coordinates.
🤝 Contributing
Contributions, issues, and feature requests are welcome!
Feel free to check the issues page.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License
Distributed under the MIT License. See LICENSE for more information.

👤 Author
Abi Angelin A

LinkedIn: www.linkedin.com/in/abiangelin

GitHub: github.com/Angel5326

Email: abiangelin814@gmail.com

<div align="center"> <i>If you found this project helpful, please give it a ⭐!</i> </div> ```
