from django.shortcuts import render

# Create your views here.

from .models import Student, Grades
def students(request):
    studentList = Student.stuObj.all()
    return render(request, 'my_app/students.html', {'students': studentList})

def addstu(request):
    grade = Grades.objects.get(pk = 1)
    stu = Student.createStudent("ass", 34, True, "dddd0", grade, '2017-8-10', '2019-2-25')
    stu.save()
    return 'abcd'