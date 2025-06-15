from django.db import models

# Create your models here.
# Migrate these models --> python3 manage.py makemigrations
#                          python3 manage.py migrate
# Sqllite setup path --> /Users/sitummohanty/PycharmProjects/djangoProject/db.sqlite3

# ======================
#  Student Model
# ----------------------
# Represents each individual student.
# Stores basic profile details: name, age, DOB, active status.
# Automatically captures the time of creation.
# One student can have many enrollments.
# ======================
class Student(models.Model):
    name = models.CharField(max_length=100)               # Student's full name
    age = models.IntegerField()                           # Student's age
    dob = models.DateField()                              # Date of birth
    is_active = models.BooleanField(default=True)         # Active/inactive flag
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of record creation

# ======================
# Course Model
# ----------------------
# Represents a course offered by the platform or institution.
# Stores course name and long-form description.
# One course can have many enrollments.
# ======================
class Course(models.Model):
    name = models.CharField(max_length=100)  # Course title
    description = models.TextField()         # Detailed course description

# ======================
# Enrollment Model
# ----------------------
# Intermediate model (junction table) for Student ↔ Course relationship.
# Represents one instance of a student enrolled in a course.
# Includes enrollment date and status flag.
# Foreign Keys:
#   - student → Student (many enrollments per student)
#   - course  → Course (many enrollments per course)
# ======================
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # FK to Student
    course = models.ForeignKey(Course, on_delete=models.CASCADE)    # FK to Course
    enroll_date = models.DateTimeField(auto_now_add=True)           # Timestamp of enrollment
    is_active = models.BooleanField(default=True)                   # Indicates if enrollment is active

# ======================
#  TestTable Model
# ----------------------
# Generic or placeholder table used for testing, temporary data, or prototyping.
# Just contains a single name field.
# Custom Meta is used to define database table name and default ordering.
# ======================
class TestTable(models.Model):
    name = models.CharField(max_length=100)  # Label or name for the test entry

"""
The class Meta: inside a Django model is used to define metadata — i.e., information about the model
that changes its behavior but isn’t itself a database field.
"""
class Meta:
    db_table = 'abc_Table'   # Custom database table name
    ordering = ['name']      # Default ordering when querying this table
