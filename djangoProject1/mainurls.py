from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path
from . import views
from . import math

urlpatterns = [
    # path('', views.sample, name='index'),
    path('search-result/', views.search, name='search'),
    path('main/', views.testing, name='testing'),
    path('main-form/', views.testing_form, name='testing_form'),
    path('math-form/', math.math_form, name='math-form'),
    path('math/', math.math, name='math'),
]