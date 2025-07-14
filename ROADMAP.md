# 🚧 Feature Roadmap – In Progress / Upcoming

---

## 🛠️ Features In Progress...

### 👩‍💼 Admin / Management

- [x] Admin analytics dashboard
- [x] Create/Manage items in department school fees

### 🧑‍🎓 Aspirants

- [x] Aspirant dashboard with admission status
- [x] Move all aspirant logic to dedicated `AspirantPortal`

---

## 🧠 Planned / Future Features (for MVP Completion)

### 🧑‍🎓 Aspirants

---

### 🎓 Students

- [ ] View results by session and semester
- [ ] View/download fee payment receipt
- [ ] Transcript and certificate generation
- [ ] Editable student profile

---

### 👨‍🏫 Academic Staff

- [ ] Dashboard to view teaching load / courses assigned
- [ ] Manage students in their assigned courses
- [ ] Upload results for assigned courses
- [ ] (For HODs) View and manage department-wide student results

---

### 🧑‍💼 Non-Academic Staff

- [ ] Role-based permission setup (secretary, bursar, admissions, etc.)
- [ ] Fee confirmation and verification dashboard
- [ ] Application reviewer (for aspirants)

---

### 👩‍💼 Admin / Management

- [ ] Add webhook to Paystack payment system for real-time updates
- [ ] Create/Manage Aspirants
- [ ] Approve or reject aspirant applications
- [ ] Promote aspirants to student users
- [ ] Assign courses to academic staff
- [ ] Assign HOD to departments
- [ ] Review and approve uploaded results
- [ ] User activity logs
- [ ] Upload and manage semester-level result summaries for students
- [ ] Implement Celery+Redis for messaging

## Later version

- [ ] Error handling in all forms like dupicate exitsts etc
- [ ] Messaging
- [ ] Real time chat using Websocket
- [ ] Aspirant Examination
- [ ] Close Aspirant Self Edit | close registration (add a field to the model an when admin checks it no more edit,
      then in template yu can just use if statement to check if the field is ticked the update btn should not show)
- [ ] batch admissin via csv, add uniq reg num to aspirant
