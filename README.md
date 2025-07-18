# 📘 University School Management System – Full Project Documentation

---

## 📝 Project Summary

**Name**: School Management System
**Framework**: Django (Python Web Framework)

**What the App Is**:
The School Management System is a multi-role web application designed to manage both academic and administrative functions in a university. It provides a unified platform where admissions, academic records, fee payments, staff functions, and overall institutional configuration can be managed securely and efficiently.

**What Problem It Solves**:

- Eliminates paper-based and disjointed workflows
- Centralizes student and staff data in a secure, scalable system
- Reduces manual errors in fee processing, result entry, and academic management
- Automates permissions and access levels for various user roles
- Increases visibility into school-wide operations for administrators

**Key Objectives**:

- Enable online student admission and tracking
- Provide students access to their academic and financial records
- Allow staff to perform teaching and non-teaching operations securely
- Grant management full oversight of the institution’s academic and administrative configuration

---

## 👥 User Roles – Who Will Use the App

The system is designed around five primary user roles, each with distinct permissions and dashboard interfaces:

### 🧑‍🎓 1. Aspirant (Prospective Student)

- Can register and apply for admission online
- Can track the status of their admission
- Can receive automated updates (e.g., approval, rejection)

### 🎓 2. Student

- Gains access upon successful admission
- Can view results, payment status, and update personal information

### 👨‍🏫 3. Academic Staff

- Lecturers and instructors responsible for specific courses
- Can enter, update, and manage student academic results

### 🧑‍💼 4. Non-Academic Staff

- Administrative personnel responsible for admissions, fees, and student services
- Can manage fee records and support aspirant onboarding

### 👩‍💼 5. Management / Admin

- Superusers and institutional heads
- Have full access to configure academic structure, manage users, and oversee operations

---

## 🔧 Server Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/university-management-system.git
cd university-management-system
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Variables

Create a `.env` file in the root directory and add the following:

```env
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=127.0.0.1,localhost

# Email (Gmail SMTP)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Paystack
PAYSTACK_SECRET_KEY=your-paystack-secret-key
PAYSTACK_PUBLIC_KEY=your-paystack-public-key
```

Ensure you use `os.environ` or `python-decouple` to load these in `settings.py`.

### 5. Database Setup

#### If Using PostgreSQL:

```bash
sudo apt install postgresql postgresql-contrib
```

In `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'yourdbname',
        'USER': 'yourdbuser',
        'PASSWORD': 'yourdbpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 6. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser

```bash
python manage.py createsuperuser
```

### 8. Collect Static Files (for production)

```bash
python manage.py collectstatic
```

### 9. Start Redis Server

```bash
sudo apt update
sudo apt install redis -y
sudo systemctl enable redis
sudo systemctl start redis
```

### 10. Start Celery Worker (for async tasks)

```bash
celery -A yourproject worker --loglevel=info
```

### 11. Start Django Development Server

```bash
python manage.py runserver
```

### 12. Run Django Channels (WebSocket Support)

Ensure `channels` is installed and `ASGI_APPLICATION` is set in `settings.py`.

Then run:

```bash
daphne yourproject.asgi:application
```

Or for development:

```bash
python manage.py runserver
```

---
