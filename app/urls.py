from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path
from django.shortcuts import HttpResponse
from app.views import home, login, signup, add, signout , delete , status

urlpatterns = [
    path('', home , name='home'),
    path('login/',login , name='login'),
    path('signup/',signup),
    path('add/',add),
    path('logout/' ,signout),
    path('delete/<int:id>',delete),
    path('status/<int:id>/<str:status>',status),
]
