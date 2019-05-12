from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . models import Grades, Student

def index(request):
    # return HttpResponse("sunck is a  ")

    return render(request, 'my_app/index.html')


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

def main(request):
    return render(request, 'my_app/main.html')

def upfile(request):
    return render(request, 'my_app/upfile.html')

## 上传文件
import os
from django.conf import settings
def savefile(request):
    if request.method == 'POST':
        f = request.FILES['file']
        #文件在服务器端的路径
        filePath = os.path.join(settings.MEDIA_ROOT, f.name)
        with open(filePath, 'wb') as fp:
            for info in f.chunks():
                fp.write(info)
        return HttpResponse('上传成功')
    else:
        return HttpResponse('上传失败')

# 学生分页
from django.core.paginator import Paginator
def stupage(request, pageid):
    allList = Student.objects.all()
    paginator = Paginator(allList, 3)
    page = paginator.page(pageid)
    return render(request, 'my_app/studentpage.html', {'students':page})


def ajaxstudents(request):
    return render(request, 'my_app/ajaxstudents.html')

#ajax
from django.http import JsonResponse
def studentsinfo(request):
    stus = Student.objects.all()
    list = []
    for stu in stus:
        list.append([stu.sname,stu.sage,stu.sgender])
    return JsonResponse({'data':list})

# 富文本
def edit(request):
    return  render(request, 'my_app/edit.html')


## celery
import time
from .task import cel
def celery(request):
    cel(request)
    return render(request, 'my_app/celery.html', {"name":"name"})