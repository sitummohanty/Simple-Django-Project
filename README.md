# Simple Django Project

A minimal Django web application demonstrating the basics of Django project and app structure, model definitions, migrations, and the Django admin interface. This project manages students, courses, and enrollments as a simple educational platform example.

---

## Features

- **Student Model:** Stores student details such as name, age, date of birth, active status, and creation timestamp.
- **Course Model:** Stores course details including name and description.
- **Enrollment Model:** Implements a many-to-many relationship between students and courses, with enrollment date and active status.
- **TestTable Model:** A generic/test model for demonstration or prototyping.
- **Django Admin Integration:** Models are registered in the Django admin for easy management.
- **Sample View:** Demonstrates how to create and save a student object.
- **Modular App Structure:** All app-specific logic is encapsulated in the `myapp` Django app.

---

## Project Structure

```
Simple-Django-Project/
│
├── djangoProject/         # Main Django project settings and configuration
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── myapp/                 # Application for managing students, courses, enrollments
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
└── manage.py              # Django project management script
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- Django 5.x (as used in the project)
- (Recommended) A virtual environment tool (e.g., `venv` or `virtualenv`)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/sitummohanty/Simple-Django-Project.git
   cd Simple-Django-Project
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install django
   ```

4. **Apply migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (for admin access):**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the app:**
    - Go to [http://127.0.0.1:8000/myapp/](http://127.0.0.1:8000/myapp/) for the basic view.
    - Go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) for the Django admin interface.

---

## Usage

- The sample view (`/myapp/`) creates and saves a new student named "Arpita" (for demonstration purposes).
- Use the Django admin to add, edit, or delete students, courses, and enrollments.

---

## Models Overview

- **Student:** `name`, `age`, `dob`, `is_active`, `created_at`
- **Course:** `name`, `description`
- **Enrollment:** `student`, `course`, `enroll_date`, `is_active`
- **TestTable:** `name`

---

## Customization

- You can expand the models and views as per your requirements.
- Add more fields or apps following the Django conventions illustrated in this template project.

---

## License

This project is for educational/demo purposes and does not include a license. Please add one if you intend to use it in production.

---

## Author

- [sitummohanty](https://github.com/sitummohanty)
