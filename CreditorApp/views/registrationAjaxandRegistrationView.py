from django.contrib.auth.hashers import make_password
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from CreditorApp.models import User


def registration(request):
    return render(request, 'creditorapp/registrationformTemplate.html', {'registration':'active'})


def registrationajaxa(request):
    if request.method == 'GET':
        date = request.GET.get('date')
        name = request.GET.get('name')
        father = request.GET.get('father')
        cell = request.GET.get('cell')
        address = request.GET.get('address')
        password = request.GET.get('password')
        #hashpassword = make_password(password=password, salt=None, hasher='md5')
        user = User.objects.create_user(cell=cell, name=name, father=father, address=address, date=date,
                                     password=password)


        user.save()


        #return JsonResponse({'success': "Data saved successfully."})
        return JsonResponse({'success': "Data save Successfully."})
    else:
        return JsonResponse({'success': "data does not save."})


