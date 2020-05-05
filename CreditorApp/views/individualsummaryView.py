from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render

from CreditorApp.models import User


def PageWisedetailview(request):

    page= request.GET.get('page')
    cursor = connection.cursor()
    q = f"SELECT cu.date,cu.name,cu.father,cu.cell,ca.cell_id,IFNULL(ca.advance,0) AS adv,IFNULL(ca.decidedrate,0) AS dr,ca.bmodel,ca.page,(ca.page||',('||ca.month || '/' || ca.day ||')') AS page,ca.date AS addate,ci.date AS cidate,ci.page_id,IFNULL(ci.amount,0) AS inst,IFNULL(ci.discount,0) AS DIS,IFNULL(ci.fine,0) AS FIN FROM creditorapp_user AS cu LEFT JOIN creditorapp_advancemotorcycle AS ca ON cu.cell = ca.cell_id LEFT JOIN creditorapp_installmentmodel AS ci ON ca.page = ci.page_id WHERE ca.page='{page}'"

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
        Decided += obj2[i]['dr']
        Advance += obj2[i]['adv']
        instalmment += obj2[i]['inst']
        fine += obj2[i]['FIN']
        discount += obj2[i]['DIS']
        # Model += obj2[i]['model']

    Total = (Decided + fine) - (Advance + instalmment + discount)
    AllValues = [Model, Decided, Advance, instalmment, discount, fine, Total]

    return render(request, 'creditorapp/pageWiseDetailTemplate.html', {'obj1': obj2, 'values': AllValues,'pagewisedetail':'active'})
    #return HttpResponse(obj2)