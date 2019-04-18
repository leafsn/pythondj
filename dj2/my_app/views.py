from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import Student, Grades
def students(request):
    studentList = Student.stuObj.all()
    return render(request, 'my_app/students.html', {'students': studentList})

# 显示前五条数据
def students1(request):
    studentList = Student.stuObj.all()[0:6]
    return render(request, 'my_app/students.html', {'students': studentList})

#分页显示
def stupage(request, page):
    # 0-5 5-10 10 -15
    # page* 5
    page = int(page)
    studentList = Student.stuObj.all()[(page -1) * 5:page * 5]
    return render(request, 'my_app/students.html', {'students': studentList})


def addstu(request):
    grade = Grades.objects.get(pk = 1)
    stu = Student.createStudent("ass", 34, True, "dddd0", grade, '2017-8-10', '2019-2-25')
    stu.save()
    return HttpResponse('abcd')

def addstudent(request):
    grade = Grades.objects.get(pk = 1)
    stu = Student.stuObj2.createStudent("111ass", 34, True, "111dddd0", grade, '2017-8-10', '2019-2-25')
    stu.save()
    return HttpResponse('abcd')

def studentsearch(request):
    studentList = Student.stuObj.filter(sname__contains = "ass")
    return render(request, 'my_app/students.html', {'students': studentList})


from django.db.models import Max, Min
def studentsearch1(request):
    maxAge = studentList = Student.stuObj.aggregate(Max('sage'))
    print(maxAge)
    return render(request, 'my_app/students.html', {'students': studentList})

from django.db.models import F, Q
def grades(request):
    g = Grades.objects.filter(ggirlnum__gt=F('gboynum'))
    print(g)
    return HttpResponse('333333')