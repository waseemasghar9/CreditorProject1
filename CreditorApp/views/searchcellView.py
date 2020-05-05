from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render



def searhcellpagefunction(request):

            cell =""
            if request.GET.get('cell'):
                cell = request.GET.get('cell')
            else:
                cell = request.user.pk


            # cell=request.GET.get('cell')

            cursor = connection.cursor()

            q= f"SELECT advan_install.date AS dt,cu.name,cu.father,cu.cell,advan_install.page AS page,advan_install.bmodel AS bm,IFNULL(advan_install.decidedrate,0) AS dr,IFNULL(advan_install.advance,0) AS adv,IFNULL(advan_install.inst1,0) AS inst,IFNULL(advan_install.DIS1,0) AS DIS,IFNULL(advan_install.FIN1,0) AS FIN FROM creditorapp_user cu LEFT JOIN (SELECT* FROM creditorapp_advancemotorcycle ca LEFT JOIN (SELECT ci.page_id, SUM(ci.amount) AS inst1,SUM(ci.discount) AS DIS1,SUM(ci.fine) AS FIN1 FROM creditorapp_installmentmodel ci GROUP BY ci.page_id) AS installment            ON ca.page= installment.page_id) AS advan_install ON cu.cell = advan_install.cell_id WHERE advan_install.cell_id='{cell}' ORDER BY advan_install.page_id"
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
               # Model += obj2[i]['bmodel']

            Total = (Decided + fine) - (Advance + instalmment + discount)
            AllValues = [Model, Decided, Advance, instalmment, discount, fine, Total]

            return  render(request, 'creditorapp/searchcellpageTemplate.html', {'obj1':obj2, 'values':AllValues,'searchcellview':'active'})          #JsonResponse(AJAXCall(whereC, mis))




















#SELECT cu.name,cu.father,cu.cell,IFNULL(SUM(ci.amount),0) AS inst,IFNULL(SUM(ci.discount),0) AS DIS,IFNULL(SUM(ci.fine),0) AS FIN,IFNULL(ca.advance,0) AS adv,IFNULL(ca.decidedrate,0) AS dr,ca.page,ca.cell_id FROM creditorapp_user AS cu LEFT JOIN creditorapp_advancemotorcycle AS ca ON cu.cell = ca.cell_id LEFT JOIN creditorapp_installmentmodel AS ci ON ca.page = ci.page_id WHERE cu.cell='03023715411' GROUP BY ci.page_id