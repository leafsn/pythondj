from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('student/', views.students),
    path('addstu', views.addstu)
]