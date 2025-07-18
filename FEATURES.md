## ✅ MVP Features – What Has Been Built

---

### 🌐 Public Pages / General Features (Non-Authenticated Users)

- University homepage with introductory content
- Undergraduate application process

---

### 🧑‍🎓 Aspirants

- Email-based registration and automatic role assignment
- Partial implementation of the online application form
- Send login credentials to newly registered aspirants via Gmail SMTP backend
- Application completion enforced using custom middleware
- Admission decision logic: Send congratulatory email to aspirant via Gmail SMTP backend upon admission
- Aspirant dashboard with admission status
- Moved all aspirant logic to dedicated `AspirantPortal`
- Admin can create/manage aspirants
- Admin can approve/reject aspirant applications
- Aspirant-to-student promotion via signal + user switch logic
- Background messaging via Celery and Redis

---

### 🎓 Students

- Personalized student dashboard
- Course registration system:
  - Register for current semester
  - View previously registered courses
- School fee management with Paystack integration:
  - Generate personalized school fee invoice
  - Make payment and get automatic confirmation
  - Track fee payment history
- View results by session and semester
- Download school fee receipt (PDF)
- Editable student profile

---

### 👩‍💼 Admin / Management

- Full CRUD for academic structure:
  - Manage faculties, departments, courses, and courses of study
  - Assign courses to specific levels
- Create and manage department-specific school fee structures
- Create and activate academic calendars
- Full user and permission management (across all roles)
- Aspirant-to-student promotion via signal logic
- Assign courses to academic staff
- Edit/delete assigned courses
- Assign HODs to departments
- Review and approve results uploaded by lecturers
- Upload and manage semester-level result summaries

---

### 👨‍🏫 Academic Staff

- Dashboard to view assigned courses (teaching load)
- Manage students in assigned courses
- Upload results for assigned courses

---

### 🧑‍💼 Non-Academic Staff

- Role-based dashboard setup
- Role-specific permission system (e.g., bursar, secretary, registrar, etc.)

---

### 📡 Real-Time Features

- Real-time chat system using Django Channels and WebSocket

---

### ⚙️ Backend Improvements

- Celery + Redis integration for background task processing
- Signals for automated role switching and aspirant promotion
- Modular structure with role-based portals (e.g., `AspirantPortal`)
