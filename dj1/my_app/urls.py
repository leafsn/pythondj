from django.contrib import admin
from django.urls import include,path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    path('grades/', views.grades),
    path('students/', views.students),

    #使用正则引入re_path
    re_path(r'^grades/(\d+)$', views.gradeStudent),
    path('main/', views.main),


    path('upfile/', views.upfile),
    path('savefile/', views.savefile),
    path('stupage/<int:pageid>/', views.stupage),
    path('ajaxstudents/', views.ajaxstudents),
    path('studentsinfo/', views.studentsinfo),

    path('edit/', views.edit),
    path('celery/', views.celery),

]