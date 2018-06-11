"""fuxin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path
from management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('home/', views.home),
    path('user/', views.user),
    path('useradd/', views.useradd),
    path('modifyuser/', views.modifyuser),
    re_path('usermodify-(?P<nid>[0-9]+).html/', views.usermodify),
    re_path('detail-(?P<nid>[0-9]+).html/', views.detailuser),


    path('addseed/', views.addseed),
    path('status/', views.status),
    path('auditer/', views.auditer),
    path('seed/', views.seed),
    path('searchseed/', views.searchseed),
    re_path('seedmodify-(?P<nid>[0-9]+).html/', views.seedmodify),
    path('modifyseed/', views.modifyseed),
    re_path('del-(?P<nid>[0-9]+).html/', views.detailseed),
    re_path('auditer-(?P<nid>[0-9]+).html/', views.auditerss),





]
