from django.shortcuts import render


def forgotpassword(request):
    return render(request, 'creditorapp/forgotpasswordformTempage.html', {})