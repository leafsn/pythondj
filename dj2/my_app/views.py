from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import F, Q
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
    # maxAge = studentList = Student.stuObj.aggregate(Max('sage'))
    # print(maxAge)

    studentList = Student.stuObj2.filter(Q(pk__lte = 3)|Q(sage__gt = 50))

    return render(request, 'my_app/students.html', {'students': studentList})


def grades(request):
    # g = Grades.objects.filter(ggirlnum__gt=F('gboynum'))
    # print(g)

    return HttpResponse('333333')

## GET
def get1(request):
    a = request.GET.get('a')
    return  HttpResponse('a' + a)

def get2(request):
    a = request.GET.getlist('a')
    return  HttpResponse('a' + a[1] + a[0])


## POST
def showregist(request):
    return render(request, 'my_app/regist.html')

def regist(request):
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    age = request.POST.get('age')
    hobby = request.POST.getlist('hobby')
    print(name)
    print(gender)
    print(age)
    print(hobby)
    return HttpResponse("post")
## response
def showresponse(request):
    res = HttpResponse()
    print(res.content)
    print(res.charset)
    print(res.status_code)
    print(res.content-type)
    return res


## cookie
def cookietest(request):
    res = HttpResponse()
    # cookie = res.set_cookie("123456",'111111')
    coo = request.COOKIES
    res.write('<h1>'+ coo +'</h1>')
    return res

# 重定向
from  django.http import HttpResponseRedirect
def redirect1(request):
    # return HttpResponseRedirect('/myapp/redirect2')
    return redirect('/myapp/redirect2')

def redirect2(request):
    return HttpResponse('abc')

def mainn(request):
    #取session
    username = request.session.get('username','游客')
    return render(request, 'my_app/mainn.html',{'username':username})

def login(request):
    return render(request, 'my_app/login.html')

def showmain(request):
    username = request.POST['username']
    #存储session
    request.session['username'] = username
    return redirect(request, '/myapp/mainn')