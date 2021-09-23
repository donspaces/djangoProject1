"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path
from . import mainurls, views
from Login import urls as lgurl
from Module import urls as dburl
from Module import specialHana
from . import loginpages

urlpatterns = [
    path('', include((mainurls, "djangoProject1"))),
    path('admin/', admin.site.urls),


    path('dbtest/', include((dburl, "Module"))),

    path('login/', include((lgurl, "Login"))),
    path('', loginpages.loginview, name="mainpage"),

    path('logout/', loginpages.logout, name="logout"),

    path('<int:luckynum>/<str:behaviour>/specialhana/', specialHana.specpage, name="hanapage"),
    path('<int:luckynum>/<str:behaviour>/specialgift/', specialHana.specgift, name="hanagift"),
    path('secret/', specialHana.secret, name="secret"),
]
