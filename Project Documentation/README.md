<div align="center">

# 🛒 Django E-Commerce Website

### Modern • Responsive • Secure • Full Stack Django Project

<img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />
<img src="https://img.shields.io/badge/Django-4.x-darkgreen?style=for-the-badge&logo=django" />
<img src="https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge&logo=postgresql" />
<img src="https://img.shields.io/badge/Stripe-Payment-635BFF?style=for-the-badge&logo=stripe" />
<img src="https://img.shields.io/badge/Bootstrap-5-purple?style=for-the-badge&logo=bootstrap" />
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3" />
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />
<img src="https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery" />
<img src="https://img.shields.io/badge/Responsive-1200px-success?style=for-the-badge" />
<img src="https://img.shields.io/badge/UI%2FUX-Modern-orange?style=for-the-badge" />
<img src="https://img.shields.io/badge/License-MIT-red?style=for-the-badge" />

</div>

---

# 🛍️ Project Overview

Welcome to my **Django E-Commerce Website**.

This project is a complete **Full Stack E-Commerce Web Application** built using the **Django Framework** with a modern, responsive, and user-friendly interface.

The application allows customers to browse products, add items to their shopping cart, place secure orders, complete online payments through **Stripe**, and manage their accounts with ease.

The project follows a modular Django architecture by separating functionalities into multiple reusable apps, making the code clean, scalable, and easy to maintain.

Every sensitive configuration such as API Keys, Database Credentials, and Django Secret Keys are securely managed using a **.env** file.

---

# ✨ Project Highlights

- 🛒 Complete E-Commerce Solution
- 👤 User Authentication System
- 💳 Stripe Payment Gateway
- 🐘 PostgreSQL Database
- 📱 Responsive Design (Optimized up to 1200px)
- ⭐ Product Review System
- 🛍️ Shopping Cart
- 📦 Order Management
- 🔐 Secure Environment Variables (.env)
- 🌱 Database Seeder (seed.py)
- 🖼️ Product Image Upload
- 🎨 Modern UI/UX Design
- ⚡ Fast and Clean Django Architecture

---

# 🚀 Features

## 👤 Authentication

- User Registration
- Secure Login
- Logout
- User Profile
- Password Protection

---

## 🛍️ Product System

- Product Listing
- Product Details
- Product Images
- Product Categories
- Product Reviews
- Related Products

---

## 🛒 Shopping Cart

- Add to Cart
- Remove Cart Items
- Update Quantity
- Dynamic Cart Total

---

## 💳 Payment

- Stripe Payment Integration
- Secure Checkout
- Order Confirmation

---

## ⭐ Reviews

- Product Ratings
- Customer Reviews

---

## 📦 Orders

- Order Placement
- Order Summary
- Checkout Process

---

## 🎨 User Experience

- Modern Design
- Responsive Layout
- Beautiful Animations
- Clean Interface
- Easy Navigation

---

# 🛠️ Built With

## Backend

- Python
- Django Framework

---

## Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- jQuery

---

## Database

- PostgreSQL

---

## Payment Gateway

- Stripe

---

## Icons

- Font Awesome
- Line Icons

---

## Fonts

- Google Fonts

---

## Image Processing

- Pillow

---

## Environment Variables

- Python-dotenv (.env)

---

# 📚 Django Applications

This project follows a modular Django architecture.

| App | Description |
|------|-------------|
| 👤 Accounts | User Authentication & Profiles |
| 🛍️ Products | Product Management |
| 🛒 Carts | Shopping Cart |
| 📦 Orders | Order Processing |
| 💳 Payments | Stripe Payment Integration |
| ⭐ Reviews | Customer Reviews |
| 🔄 Shared | Shared Utilities & Common Components |

---

# 🌟 Project Goals

The primary objective of this project is to build a modern E-Commerce platform that demonstrates real-world Django development practices.

The project focuses on:

✅ Clean Code Structure

✅ Scalable Django Architecture

✅ Secure Authentication

✅ Responsive UI

✅ Beautiful User Experience

✅ Database Design

✅ Payment Integration

✅ Production Ready Development

---

# 📖 Table of Contents

- Project Overview
- Features
- Tech Stack
- Django Applications
- Installation Guide
- Requirements
- Environment Variables
- PostgreSQL Configuration
- Stripe Configuration
- Project Structure
- Folder Structure
- Media Files
- Static Files
- Responsive Design
- Available Pages
- Database Seeder
- Screenshots
- Future Improvements
- License
- Author

---

> 📌 **Note:** This project is built for educational purposes and portfolio demonstration. It follows modern Django development practices and showcases a complete full-stack e-commerce workflow with authentication, cart management, order processing, payment integration, and responsive UI/UX design.

---

# 🚀 Installation Guide

Follow the steps below to run this project on your local machine.

---

# 📌 Prerequisites

Before running this project, make sure the following software is installed on your computer.

| Software | Version |
|----------|---------|
| Python | 3.11+ Recommended |
| Git | Latest |
| PostgreSQL | Latest |
| VS Code | Recommended |
| pip | Latest |

---

# 🐍 Step 1 — Install Python

Download and install the latest version of Python from the official website.

🔗 https://www.python.org/downloads/

> **Important:** During installation, make sure to check the box:

```
✅ Add Python to PATH
```

After installation, verify it:

```bash
python --version
```

or

```bash
python3 --version
```

---

# 📥 Step 2 — Install Git

Download Git from:

🔗 https://git-scm.com/downloads

Verify installation:

```bash
git --version
```

---

# 💻 Step 3 — Install Visual Studio Code

Download VS Code:

🔗 https://code.visualstudio.com/

Recommended Extensions:

- Python
- Django
- Pylance
- GitLens
- Bootstrap IntelliSense
- HTML CSS Support

---

# 📂 Step 4 — Clone the Repository

```bash
git clone https://github.com/your-username/your-repository.git
```

Go inside the project folder.

```bash
cd your-repository
```

---

# 📦 Step 5 — Create Virtual Environment

Windows

```bash
python -m venv venv
```

Mac/Linux

```bash
python3 -m venv venv
```

---

# ▶️ Step 6 — Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

After activation your terminal should look like:

```text
(venv) C:\Project>
```

---

# 📥 Step 7 — Install Required Packages

```bash
pip install -r requirements.txt
```

Verify installed packages

```bash
pip list
```

---

# 🐘 Step 8 — Install PostgreSQL

Download PostgreSQL:

🔗 https://www.postgresql.org/download/

During installation remember your:

- Database Name
- Username
- Password
- Port

Example

```
Database : ecommerce_db

Username : postgres

Password : ********

Port : 5432
```

---

# 🔐 Step 9 — Configure Environment Variables

Create a file named

```
.env
```

Example:

```env
SECRET_KEY=your_secret_key

DEBUG=True

DB_NAME=ecommerce_db

DB_USER=postgres

DB_PASSWORD=your_password

DB_HOST=localhost

DB_PORT=5432

STRIPE_PUBLIC_KEY=pk_test_xxxxxxxxxxxxxxxxxx

STRIPE_SECRET_KEY=sk_test_xxxxxxxxxxxxxxxxxx
```

> Never upload your `.env` file to GitHub.

---

# 🗄️ Step 10 — Apply Database Migrations

```bash
python manage.py makemigrations
```

Then

```bash
python manage.py migrate
```

---

# 👤 Step 11 — Create Superuser

```bash
python manage.py createsuperuser
```

Enter

- Username
- Email
- Password

---

# 🌱 Step 12 — Seed the Database

This project includes a `seed.py` file for generating sample data.

Run the seed file according to your project configuration.

Example:

```bash
python seed.py
```

---

# ▶️ Step 13 — Run Development Server

```bash
python manage.py runserver
```

Open your browser

```
http://127.0.0.1:8000/
```

---

# 💳 Stripe Configuration

This project uses **Stripe** as the payment gateway.

Create a free Stripe account.

🔗 https://dashboard.stripe.com/

Copy your:

- Publishable Key

- Secret Key

and place them inside the `.env` file.

Example

```env
STRIPE_PUBLIC_KEY=pk_test_xxxxxxxxxxxxxxxxx

STRIPE_SECRET_KEY=sk_test_xxxxxxxxxxxxxxxxx
```

---

# 📁 Media Files

Uploaded images are stored inside

```
media/
```

The project uses **Pillow** to process image uploads.

---

# 📂 Static Files

All static resources are organized inside the `static/` directory.

Including:

- CSS
- JavaScript
- Bootstrap
- Icons
- Fonts
- Images

---

# ⚠️ Important Notes

- Keep your virtual environment activated while working.
- Never push your `.env` file to GitHub.
- Always install packages from `requirements.txt`.
- PostgreSQL must be running before starting the Django server.
- Stripe API keys should always remain private.
- Product images require the Pillow package.
- Make sure all migrations are applied before running the project.

---

# ✅ Successfully Installed!

If everything is configured correctly, your project should now be running at:

```
http://127.0.0.1:8000/
```

🎉 Congratulations! Your Django E-Commerce project is now ready for development.


# 📦 Python Requirements

Install all required packages using the following command:

```bash
pip install -r requirements.txt
```

### requirements.txt

```txt
Django>=4.2

Pillow

psycopg2-binary

python-dotenv

stripe

django-crispy-forms

crispy-bootstrap5

gunicorn

whitenoise
```

---

# 🏗️ Project Structure

```text
Django-Ecommerce/
│
├── accounts/
│
├── carts/
│
├── products/
│
├── orders/
│
├── payments/
│
├── reviews/
│
├── shared/
│
├── media/
│
├── static/
│   ├── css/
│   ├── javascript/
│   ├── images/
│   ├── bootstrap/
│   └── fonts/
│
├── templates/
│   ├── accounts/
│   ├── carts/
│   ├── products/
│   ├── orders/
│   ├── payments/
│   ├── reviews/
│   ├── shared/
│   └── errors/
│
├── ecommerce/
│
├── .env
├── .gitignore
├── manage.py
├── requirements.txt
├── seed.py
└── README.md
```

---

# 📂 Django Applications

The project is divided into multiple reusable Django applications.

## 👤 Accounts

Responsible for:

- User Registration
- Login
- Logout
- Profile
- Authentication
- User Information

---

## 🛍️ Products

Responsible for:

- Product Listing
- Product Details
- Categories
- Product Images
- Product Information

---

## 🛒 Carts

Responsible for:

- Shopping Cart
- Quantity Update
- Remove Items
- Total Calculation

---

## 📦 Orders

Responsible for:

- Checkout
- Order Creation
- Order History
- Order Summary

---

## 💳 Payments

Responsible for:

- Stripe Payment
- Payment Verification
- Secure Checkout

---

## ⭐ Reviews

Responsible for:

- Product Ratings
- Customer Reviews
- Feedback System

---

## 🔄 Shared

Contains common resources used throughout the project.

Examples:

- Shared Views
- Utilities
- Common Context
- Reusable Components

---

# 📱 Responsive Design

This project has been carefully designed to provide an excellent user experience across different screen sizes.

### Optimized for

✅ Desktop

✅ Laptop

✅ Tablet

✅ Large Mobile Devices

The UI is fully responsive and optimized up to:

```text
1200px Screen Width
```

Bootstrap Grid System has been used extensively to create a flexible and responsive layout.

---

# 🎨 UI / UX

Special attention has been given to the user experience.

Highlights include:

- Modern Layout
- Clean Typography
- Beautiful Color Combination
- Smooth User Navigation
- Consistent Design Language
- Well Structured Components
- Easy-to-use Interface
- Interactive Buttons
- Responsive Cards
- Product Hover Effects
- Attractive Hero Sections
- Professional Footer Design

---

# 🖼️ Image Management

Product images are handled using the **Pillow** package.

Uploaded images are stored inside the:

```text
media/
```

directory.

---

# 🎯 Google Fonts

This project uses Google Fonts to improve typography and readability.

Fonts are loaded directly from Google's CDN.

---

# 🎨 Icons

The project uses:

- Font Awesome
- Line Icons

to provide a modern interface.

---

# 📄 Available Pages

This project currently contains **15+ pages**, including:

- 🏠 Home Page
- 🛍️ Product Page
- 📄 Product Details Page
- 🔍 Search Page
- 🛒 Shopping Cart
- 💳 Checkout Page
- 📦 Order Page
- 👤 User Profile
- 🔐 Login Page
- 📝 Registration Page
- ⭐ Review Section
- ❌ Custom 404 Error Page
- 📬 Contact Section
- 📃 Terms & Policies
- 📱 Responsive Navigation

…and several reusable shared templates.

---

# 🔐 Security

Security has been considered throughout the project.

Features include:

- Environment Variables (.env)
- Hidden Secret Keys
- Secure Stripe Keys
- Django CSRF Protection
- Secure Authentication
- Protected User Sessions

Sensitive information is **never hardcoded** into the source code.

---

# 🌱 Database Seeder

A custom:

```text
seed.py
```

file is included to quickly populate the database with sample data.

This helps developers test the application without manually creating products and records.

---

# 🗄️ Database

The project uses:

## PostgreSQL

Benefits:

- Fast
- Reliable
- Production Ready
- Highly Scalable
- Secure
- ACID Compliant

---

# 🚀 Why This Project?

This project was developed to demonstrate real-world Django development practices.

It showcases how to build a complete E-Commerce platform using a clean architecture and modern web technologies.

The project emphasizes:

✅ Clean Code

✅ Modular Architecture

✅ Reusable Components

✅ Responsive Design

✅ Secure Development

✅ Database Design

✅ Payment Gateway Integration

✅ User Experience

✅ Scalable Project Structure

---

# 💡 Development Philosophy

This project follows best practices for Django development:

- Separation of Concerns
- Reusable Django Apps
- Organized Templates
- Static & Media Management
- Environment Variable Security
- Clean Project Structure
- Easy Maintenance
- Future Scalability

---

> ❤️ This project is continuously being improved with new features, performance optimizations, and UI/UX enhancements.

---

# 📸 Project Screenshots

> **Note:** Add screenshots of your project here to showcase the user interface.

## 🏠 Home Page

<p align="center">
<img src="screenshots/home.png" width="100%">
</p>

---

## 🛍️ Product Page

<p align="center">
<img src="screenshots/products.png" width="100%">
</p>

---

## 📄 Product Details

<p align="center">
<img src="screenshots/product-details.png" width="100%">
</p>

---

## 🛒 Shopping Cart

<p align="center">
<img src="screenshots/cart.png" width="100%">
</p>

---

## 💳 Checkout

<p align="center">
<img src="screenshots/checkout.png" width="100%">
</p>

---

## 👤 User Profile

<p align="center">
<img src="screenshots/profile.png" width="100%">
</p>

---

# 🌍 Deployment

This project can be deployed on various cloud platforms, including:

- Render
- Railway
- PythonAnywhere
- DigitalOcean
- VPS
- AWS EC2

---

# 🚀 Future Improvements

The project is actively growing. Planned features include:

- ❤️ Wishlist System
- 🎟️ Coupon & Discount Management
- 📦 Order Tracking
- 📧 Email Verification
- 🔔 Email Notifications
- 📱 Progressive Web App (PWA)
- 🌐 REST API
- 📊 Admin Dashboard Analytics
- 💬 Live Chat Support
- ❤️ Favorite Products
- 🔍 Advanced Product Filters
- 🌍 Multi-language Support
- 💱 Multi-Currency Support
- 📱 Mobile Application Integration

---

# 🎯 Key Features

| Feature | Status |
|----------|--------|
| User Authentication | ✅ |
| Product Management | ✅ |
| Shopping Cart | ✅ |
| Stripe Payment | ✅ |
| PostgreSQL | ✅ |
| Product Reviews | ✅ |
| Responsive Design | ✅ |
| Modern UI/UX | ✅ |
| Environment Variables (.env) | ✅ |
| Media Upload | ✅ |
| Bootstrap 5 | ✅ |
| jQuery | ✅ |
| Google Fonts | ✅ |
| Font Awesome | ✅ |
| Line Icons | ✅ |
| Database Seeder | ✅ |

---

# 📈 Project Statistics

| Information | Details |
|-------------|----------|
| Framework | Django |
| Language | Python |
| Database | PostgreSQL |
| Payment Gateway | Stripe |
| Responsive | Yes (1200px Optimized) |
| Pages | 15+ |
| Django Apps | 7 |
| Authentication | Django Authentication |
| Environment Variables | .env |
| Image Processing | Pillow |

---

# 🤝 Contributing

Contributions are always welcome!

If you'd like to improve this project:

1. Fork the repository
2. Create your feature branch

```bash
git checkout -b feature/NewFeature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push your branch

```bash
git push origin feature/NewFeature
```

5. Open a Pull Request

---

# 🐛 Report Issues

If you find any bugs or have suggestions, please create an Issue on GitHub.

Your feedback is greatly appreciated.

---

# ⭐ Support This Project

If you found this project useful, please consider giving it a ⭐ on GitHub.

It really helps and motivates future development.

<p align="center">

## ⭐⭐⭐⭐⭐

### Don't forget to Star this Repository!

</p>

---

# 📜 License

This project is released under the **MIT License**.

You are free to use, modify, and distribute this project for educational and personal purposes.

---

# 👨‍💻 Author

## Developer Rayhan

**Full Stack Django Developer**

Passionate about building modern, responsive, and scalable web applications using Python and Django.

---

# 📬 Contact

📧 Email

```text
iamdeveloperrayhan@gmail.com
```

💼 LinkedIn

```text
https://linkedin.com/in/iamdeveloperrayhan
```

🐙 GitHub

```text
https://github.com/iamdeveloperrayhan
```

---

# 🙏 Acknowledgements

Special thanks to the amazing open-source community and the creators of:

- Python
- Django
- PostgreSQL
- Bootstrap
- Stripe
- Font Awesome
- Line Icons
- Google Fonts

for providing incredible tools that made this project possible.

---

<div align="center">

# ❤️ Thank You for Visiting!

### If you enjoyed this project, don't forget to ⭐ Star the repository!

<img src="https://img.shields.io/github/stars/your-username/your-repository?style=for-the-badge">

<img src="https://img.shields.io/github/forks/your-username/your-repository?style=for-the-badge">

<img src="https://img.shields.io/github/issues/your-username/your-repository?style=for-the-badge">

<img src="https://img.shields.io/github/license/your-username/your-repository?style=for-the-badge">

<br><br>

### 🚀 Happy Coding!

</div>
