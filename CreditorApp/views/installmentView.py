import json

from django.db import connection
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from CreditorApp.models import AdvanceMotorcycle, InstallmentModel


def installmentform(request):

    if not request.user.is_authenticated:
        return redirect('../logintemplate/')
    else:

        return render(request, 'creditorapp/installmentformTemplate.html', {'installmentForm':'active'})

def installmentdataAJX(request):
    page = request.GET.get('page')
    date = request.GET.get('date')
    amount = request.GET.get('amount')
    discount = request.GET.get('discount')
    fine = request.GET.get('fine')


    pageExist =  AdvanceMotorcycle.objects.filter(page=page)
    if pageExist:
        installmenObject=InstallmentModel(page_id=page, date=date,amount=amount,discount=discount,fine=fine)
        installmenObject.save()
        return JsonResponse({'success':"Data saves successfully."})
    else:
        return JsonResponse({'success': "page does not exist"})

#this function is used to check page.

def installmentPageCheckAJX(request):
    page = request.GET.get('page')
    cursor = connection.cursor()
    q = f"SELECT ci.date ,ca.page,IFNULL(ca.decidedrate,0) AS dr,IFNULL(ca.advance,0) AS adv,IFNULL(ci.amount,0) AS inst,IFNULL(ci.discount,0) AS DIS,IFNULL(ci.fine,0) AS FIN FROM creditorapp_advancemotorcycle ca LEFT JOIN creditorapp_installmentmodel ci ON ca.page = ci.page_id WHERE ca.page='{page}' ORDER BY ci.date"
    cursor.execute(q)

    objs = cursor.fetchall()
    obj1 = cursor.description
    obj2 = []
    for r in objs:
        i = 0
        d = {}
        while i < len(obj1):
            d[obj1[i][0]] = r[i]
            i = i + 1
        obj2.append(d)






    pageExist =  AdvanceMotorcycle.objects.filter(page=page)
    if pageExist:
        # o = json.dumps(obj2)
        return JsonResponse({'success':"You may continue.", 'data1':objs})
    else:
        return JsonResponse({'success': "page does not exist"})