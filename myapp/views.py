from django.shortcuts import render
from datetime import date
# Create your views here.
from django.http import HttpResponse
from myapp.models import Student

def index(request):
	s1 = Student(name="Arpita", age=30, dob=date.today())
	s1.save()  # save to db..

	# student = Student.objects.get(name="Arpita")
	# student.age = 10
	# student.save()
	return HttpResponse(f"Django app started")