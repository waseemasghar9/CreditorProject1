from django.contrib import auth, messages
from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render, redirect


def showloginpage(request):
    if request.method=='POST':
        cell = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate( username=cell, password=password)
        if user is not None:
            auth.login(request,user)

            if request.user.is_admin:
                return  redirect('../aggregatePage/')
            elif request.user.is_owner:
                return redirect('../aggregatePage/')
            else:
                cell=request.user.pk
                return redirect('../searchcellpage/?cell='+cell)
        else:
            messages.error(request,"Invalid Credential..")
            return render(request, 'creditorapp/loginpageformTemplate.html', {'failed': 'Invalid Credential...'})
        #show pag
    else:

        return render(request, 'creditorapp/loginpageformTemplate.html', {'login':'active'})


def logout1(request):
    logout(request)

    
    #return redirect('../logintemplate/',{'logout':'logoue'})
    return render(request, 'creditorapp/loginpageformTemplate.html', {'login': 'active'})

