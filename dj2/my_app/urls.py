from django.contrib import admin
from django.urls import path, re_path

from . import views
urlpatterns = [
    path('student/', views.students),
    path('addstu/', views.addstu),
    path('addstudent', views.addstudent),
    path('student1', views.students1),
    re_path(r'^stu/(\d+)/$', views.stupage),
    path('studentsearch', views.studentsearch),
    path('studentsearch1', views.studentsearch1),
    path('grades', views.grades),

    path('get1/', views.get1),
    path('get2/', views.get2),

    path('showregist/', views.showregist),
    path('showregist/regist/', views.regist),
    path('cookietest/', views.cookietest),

    path('redirect1/', views.redirect1),
    path('redirect2/', views.redirect2),
    path('mainn/', views.mainn),
    path('login/', views.login),
    re_path(r'^showmain/$', views.showmain),
]