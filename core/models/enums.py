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
