from django.contrib import admin
from myapp.models import Student, Course, Enrollment

# ================================
# Django Admin Registration
# -------------------------------
# This registers your models so you can
# manage them via the Django Admin interface.
# The admin panel is accessible at /admin/
# ================================

# ▶ Registering Course model
admin.site.register(Course)

# ▶ Registering Enrollment model
admin.site.register(Enrollment)


# ================================
# Customize Admin Panel
# -------------------------------
# You can use `ModelAdmin` to define how each
# model appears in the admin dashboard.
# Example shown below (uncomment to use)
# ================================

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'dob', 'is_active', 'created_at')  # fields to show in list view
    search_fields = ('name',)            # adds search box for 'name'
    list_filter = ('is_active',)         # adds filter sidebar for active status