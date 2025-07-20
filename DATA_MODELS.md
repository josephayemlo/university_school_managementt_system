# 🧩 Django Backend Data Models – School Management System

## 📦 App: application

---

## Model: PersonalStatement

- personal_statement
- title

## Model: UndergraduateApplication

- first_name, last_name, gender, dob, email
- phone_number, address_1, address_2, city
- state_province, postal_code, country, course_of_study

## Model: ScholarshipApplication

- Remove this Model

---

## 📦 App: aspirantportal

---

## 📦 App: core (Central Application for all applications )

---

## Models/user start

## 🔐 Custom User Manager – CustomUserManager

- Overrides create_user and create_superuser
- Used by CustomUser for email-based authentication

---

## Model: CustomUser

- email, user_type, gender, address
- created_at, updated_at
- username = None (uses email instead)
- USERNAME_FIELD = "email", REQUIRED_FIELDS = []
- choices: user_type (1–5), gender (M/F)
- manager: CustomUserManager

---

## Model: AspirantStudent

- admin (OneToOne to CustomUser), course_applied (FK)
- phone_number, address_1, address_2, city, state_province, postal_code, country
- admission_status (choices: pending, admitted, rejected)

- school_name, school_address_1, school_address_2, school_city, school_state_province
- school_postal_code, school_year_graduated

- emergency_first_name, emergency_last_name, emergency_email, emergency_phone_number
- emergency_address_1, emergency_address_2, emergency_city, emergency_postal_code
- emergency_country, emergency_relationship (choices: B, S, F, M, O)

- referee_first_name, referee_last_name, referee_email, referee_phone_number
- referee_address_1, referee_address_2, referee_city, referee_postal_code
- referee_state_province, referee_country

---

## Model: Student

- admin (OneToOne to CustomUser), matric_no (unique)
- course_of_study (FK), level (choices from LevelChoices)
- date_of_admission (auto_now_add)

---

## Model: AcademicStaff

- admin (OneToOne to CustomUser)
- position
- role
- department

---

## Model: NonAcademicStaff

- admin (OneToOne to CustomUser)
- role

## Models/user end

---

## Models/shared start

## Model: Faculty

- name (unique)

---

## Model: Department

- name, faculty (FK)
- unique together: (name, faculty)

---

## Model: CourseOfStudy

- name, department (FK)
- duration_years (default: 4)
- unique together: (name, department)

---

## Model: Course

- code, title, unit
- level (choices from LevelChoices), semester (SemesterChoices)
- department (FK), category (CourseCategoryChoices)
- created_at, updated_at

---

## Model: AcademicCalendar

- session (e.g., '2024/2025')
- semester (SemesterChoices), is_current (bool)

---

## Model: RegisteredCourse

- student (FK), course (FK), academic_calendar (FK)
- approved (bool), approved_by (FK to User), approved_at
- is_repeat_course, is_locked, timestamp

---

## Model: LevelCourse

- course (FK), level (LevelChoices), semester (SemesterChoices)
- course_of_study (FK), is_compulsory (bool)
- unique together: (level, semester, course, course_of_study)

---

## Model: StudentResult

- registered_course (OneToOne)
- ca1, ca2, ca3, exam
- grade_point, remark, is_released
- created_at, updated_at, updated_by (FK to User)

---

## Model: SemesterResult

- student (FK),
- academic session(FK to Acdemic Calendar)
- total registered units
- total units passed
- toal grade point
- gpa, cgpa, remark, is_released, updated at

## Models/shared end

---

## Models/school_fees_payment start

## Model: DepartmentSchoolFee

- department (FK to Department)
- academic_calendar (FK to AcademicCalendar)
- level (LevelChoices)
- total_amount (auto-updated via fee items)
- created_at

---

## Model: DepartmentFeeItem

- department_school_fee (FK)
- title (e.g., Tuition, Medicals)
- amount

---

## Model: StudentSchoolFee

- student (FK to Student)
- department (FK to Department)
- academic_calendar (FK to AcademicCalendar)
- level
- total_amount
- is_paid (bool)
- reference (unique, auto-generated)
- status: ['pending', 'success', 'failed']
- last_payment_attempt
- generated_at

---

## Model: SchoolFeeItem

- student_fee (FK to StudentSchoolFee)
- name (e.g., Tuition)
- amount

---

## Model: FailedPayment

- student (FK to Student)
- department (FK to Department)
- academic_calendar (FK to AcademicCalendar)
- level
- total_amount
- reference (unique, auto-generated)
- generated_at

## Models/school_fees_payment end

---

## Models/Enums start

## Enum: LevelChoices (Enum)

- LEVEL_100, LEVEL_200, ..., LEVEL_600

---

## Enum: CourseCategoryChoices (Enum)

- Core, Elective, General

---

## Enum: SemesterChoices (Enum)

- First, Second

## Models/Enums end

---
