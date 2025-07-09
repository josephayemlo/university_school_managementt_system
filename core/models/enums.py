# Using Textchoice gives advantage fo logic comparison in view making it better option over tuple
from django.db import models


# Level Choices (IntegerChoices)

class LevelChoices(models.TextChoices):
    LEVEL_100 = '100', '100 Level'
    LEVEL_200 = '200', '200 Level'
    LEVEL_300 = '300', '300 Level'
    LEVEL_400 = '400', '400 Level'
    LEVEL_500 = '500', '500 Level'

# Course Category (TextChoices)
class CourseCategoryChoices(models.TextChoices):
    CORE = 'core', 'Core'
    ELECTIVE = 'elective', 'Elective'
    GENERAL = 'general', 'General'


# Semester (TextChoices)
class SemesterChoices(models.TextChoices):
    FIRST = 'First', 'First Semester'
    SECOND = 'Second', 'Second Semester'

class AcademicStaffPosition(models.TextChoices):
    PROFESSOR = 'PROF', 'Professor'
    ASSOCIATE_PROFESSOR = 'ASSOC_PROF', 'Associate Professor'
    SENIOR_LECTURER = 'SR_LECT', 'Senior Lecturer'
    LECTURER_I = 'LECT_I', 'Lecturer I'
    LECTURER_II = 'LECT_II', 'Lecturer II'
    ASSISTANT_LECTURER = 'ASST_LECT', 'Assistant Lecturer'
    GRADUATE_ASSISTANT = 'GRAD_AST', 'Graduate Assistant'

    
class AcademicStaffRole(models.TextChoices):
    HOD = 'HOD', 'Head of Department'
    DEAN = 'DEAN', 'Dean'
    EXAM_OFFICER = 'EXAM_OFFICER', 'Examination Officer'
    STAFF = 'STAFF', 'Regular Staff'

class NonAcademicStaffRole(models.TextChoices):
    REGISTRAR = 'REGISTRAR', 'Registrar'
    BURSAR = 'BURSAR', 'Bursar'
    LIBRARIAN = 'LIBRARIAN', 'Librarian'
    ICT_OFFICER = 'ICT_OFFICER', 'ICT Officer'
    SECURITY = 'SECURITY', 'Security Staff'
    CLEANER = 'CLEANER', 'Cleaner'
    CLERK = 'CLERK', 'Clerical Staff'
    STAFF = 'STAFF', 'Regular Staff'
