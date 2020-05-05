"""CreditorProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from CreditorApp import views

urlpatterns = [
#showloginpageView.py
path('logintemplate/',views.showloginpage, name='loginsuccess'),
path('forgotpassword/',views.forgotpassword , name = 'forgotpassword'),#path('loginsuccess/',views.loginsuccess , name = 'login'),

#registrationAjaxandRegistrationView.py
path('registration/',views.registration , name = 'registration'),
path('registrationajaxa/',views.registrationajaxa , name = 'registrationajax'),

#usernameCheckView.py
path('usernamecheck/',views.usernamecheck, name= 'usernamecheck'),
#advancemotorcycleView.py
path('advancemotorcycle/',views.advancemotorcycle,name='advancemotorcycel'),
path('advancemotorcycledata/',views.advancemotorcycledataAJX,name='advancemotorcyceldata'),
path('Cell_PageExsit/',views.Cell_PageExistAJX,name='Cell_PageExist'),

#installmentView.py
path('installmentdata/', views.installmentdataAJX,name='installmentdata'),
path('installmentform/',views.installmentform, name='installmentform'),
path('installmentpagecheck/', views.installmentPageCheckAJX,name='installmentpagecheck'),
#aggregateView.py
path('aggregatePage/',views.aggregateFucntion, name='aggregatepage'),
path('aggregateAJAX',views.aggregateAJAX,name='aggregateAJAX'),

#searchcellView.py
path('searchcellpage/', views.searhcellpagefunction, name='searchcellpage'),

#pageWiseDetailView.py
path('pageWiseDetailUlr/', views.PageWisedetailview, name='pagewisedetail'),

#registrationAjaxandRegistrationView.py
path('logoutpage/', views.logout1, name='logoutpage'),


]
