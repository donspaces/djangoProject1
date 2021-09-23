from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('wikipage/<str:pk>', DetailView.as_view(), name="wiki"),
    path('common/', dbtest, name="dbcommon"),
    path('committed/', commit, name="dbcommit"),
    path('search/', select, name="dbsearch"),
    path('deleted/', delete, name="dbdelete"),
]