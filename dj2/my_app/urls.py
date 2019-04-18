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
    path('grades', views.grades)
]