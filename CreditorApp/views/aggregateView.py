from django.contrib.auth.decorators import login_required
from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render
from django_pivot.pivot import pivot
from django_pivot.histogram import histogram

from CreditorApp.models import User


def aggregateFucntion(request):

    cursor = connection.cursor()
    q = f"SELECT cu.date,cu.name,cu.father,cu.cell,IFNULL(adinst.decided,0) AS d,IFNULL(adinst.adv,0) AS a,IFNULL(adinst.am2,0) AS am,IFNULL(adinst.dicount,0) AS dis,IFNULL(adinst.fine,0) AS f, IFNULL(adinst.m,0) AS model FROM creditorapp_user cu LEFT JOIN (SELECT advance1.cell_id,SUM(advance1.dr) AS decided,SUM(advance1.ad) AS adv,COUNT(advance1.model) AS m,SUM(installment.am) AS am2,SUM(installment.f) AS fine,SUM(installment.dis) AS dicount  FROM (SELECT ca.page, ca.cell_id,SUM(ca.decidedrate) AS dr,SUM(ca.advance) AS ad,COUNT(ca.bmodel) AS model FROM creditorapp_advancemotorcycle ca GROUP BY ca.page) AS advance1 LEFT JOIN (SELECT page_id,SUM(amount) AS am,SUM(fine) AS f, SUM(discount) AS dis FROM creditorapp_installmentmodel GROUP BY page_id) AS installment ON advance1.page= installment.page_id GROUP BY advance1.cell_id) AS adinst ON cu.cell=adinst.cell_id"
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

    Decided, Advance, Model, instalmment, fine, discount = 0, 0, 0, 0, 0, 0

    for i in range(len(obj2)):
        Decided += obj2[i]['d']
        Advance += obj2[i]['a']
        instalmment += obj2[i]['am']
        fine += obj2[i]['f']
        discount += obj2[i]['dis']
        Model += obj2[i]['model']

    Total = (Decided + fine) - (Advance + instalmment + discount)
    AllValues = [Model, Decided, Advance, instalmment, discount, fine, Total]

    return render(request, 'creditorapp/aggregateTemplate.html', {'obj1': obj2, 'values': AllValues,'aggregateTemplate':'active'})


def aggregateAJAX(request):

        def AJAXCall(whereC,cell):
            cursor = connection.cursor()
            q = f"SELECT cu.date,cu.name,cu.father,cu.cell,IFNULL(adinst.decided,0) AS d,IFNULL(adinst.adv,0) AS a,IFNULL(adinst.am2,0) AS am,IFNULL(adinst.dicount,0) AS dis,IFNULL(adinst.fine,0) AS f, IFNULL(adinst.m,0) AS model FROM creditorapp_user cu LEFT JOIN (SELECT advance1.cell_id,SUM(advance1.dr) AS decided,SUM(advance1.ad) AS adv,COUNT(advance1.model) AS m,SUM(installment.am) AS am2,SUM(installment.f) AS fine,SUM(installment.dis) AS dicount  FROM (SELECT ca.page, ca.cell_id,SUM(ca.decidedrate) AS dr,SUM(ca.advance) AS ad,COUNT(ca.bmodel) AS model FROM creditorapp_advancemotorcycle ca GROUP BY ca.page) AS advance1 LEFT JOIN (SELECT page_id,SUM(amount) AS am,SUM(fine) AS f, SUM(discount) AS dis FROM creditorapp_installmentmodel GROUP BY page_id) AS installment ON advance1.page= installment.page_id GROUP BY advance1.cell_id) AS adinst ON cu.cell=adinst.cell_id where {whereC}='{cell}'"
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
            Decided, Advance, Model, instalmment, fine, discount = 0, 0, 0, 0, 0, 0
            for i in range(len(obj2)):
                Decided += obj2[i]['d']
                Advance += obj2[i]['a']
                instalmment += obj2[i]['am']
                fine += obj2[i]['f']
                discount += obj2[i]['dis']
                Model += obj2[i]['model']

            Total = (Decided + fine) - (Advance + instalmment + discount)
            AllValues = [Model, Decided, Advance, instalmment, discount, fine, Total]
            return {'values': objs,'Total':AllValues}

        cell=request.GET.get('cell')
        name = request.GET.get('name')
        father = request.GET.get('father')
        mis =""
        whereC=""
        if cell != "":
            mis=cell
            whereC = "cu.cell"
        elif name != "":
            mis = name
            whereC = "cu.name"
        elif father != "":
            mis =father
            whereC = "cu.father"
        return JsonResponse(AJAXCall(whereC,mis))
       # return JsonResponse({'values': objs,'Total':AllValues})
