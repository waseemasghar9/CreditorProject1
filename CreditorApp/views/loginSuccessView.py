from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render

# this page is not user anymore.
# def loginsuccess(request):
#     cell = request.POST.get('username')
#     password = request.POST.get('password')
#     user = auth.authenticate(request=None, username=cell, password=password)
#     # if user is not None:
#     #     return render(request, 'creditorapp/loginpageformTemplate.html', {'success': 'Succeeded'})
#     # else:
#     #     return render(request, 'creditorapp/loginpageformTemplate.html', {'success': password})
#
#     return HttpResponse(user.user_permissions)