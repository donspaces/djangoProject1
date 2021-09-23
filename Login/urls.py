from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path

from . import views

urlpatterns=[
    path('loginpage/', views.loginpage, name="login"),
    path('signuppage/',views.signuppage, name="sign_up"),

    path('verifyemail/?name=<str:username>', views.emailpage, name="verify"),
    path('verified/?name=<str:username>/?code=<str:passcode>', views.verifypage, name="success")
]