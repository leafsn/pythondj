from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . models import Grades, Student

def index(request):
    return HttpResponse("sunck is a  ")



def grades(request):
    #模板中取数据
    gradesList = Grades.objects.all()
    #将数据传递给模板, 模板再渲染页面,将渲染好的页面返回
    return render(request, 'my_app/grades.html', {"grades":gradesList})


def students(request):
    studentsList = Student.objects.all()
    return render(request, 'my_app/students.html', {'students':studentsList})


def gradeStudent(request, num):
    #获得对应的班级对象
    grade = Grades.objects.get(pk = num)
    studentsList = grade.student_set.all()
    return render(request, "my_app/students.html",{'students':studentsList})