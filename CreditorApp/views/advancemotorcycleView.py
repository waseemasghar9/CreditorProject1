from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render

from CreditorApp.models import User, AdvanceMotorcycle

#to show Advance motorcyle form
def advancemotorcycle(request):
    return render(request, 'creditorapp/AdvanceMotorCycleForm.html', {'advanceform':'active'})

def advancemotorcycledataAJX(request):
    cell = request.GET.get('cell')
    cellExist = User.objects.filter(cell=cell)
    if cellExist:
        page = request.GET.get('page')
        pageExist = AdvanceMotorcycle.objects.filter(page=page)
        if not pageExist:
            page = request.GET.get('page')
            date = request.GET.get('date')
            page = request.GET.get('page')
            bmodel = request.GET.get('bmodel')
            drate = request.GET.get('drate')
            advance = request.GET.get('advance')
            month = request.GET.get('month')
            day = request.GET.get('day')
            advancemotorcyeleObject = AdvanceMotorcycle(cell_id=cell, date=date, page=page, bmodel=bmodel, decidedrate=drate,
                                                        advance=advance,month=month,day=day)
            advancemotorcyeleObject.save()
            return JsonResponse({'success': "Data Save Successfullyaaa."})
        else:

            return JsonResponse({'success': "Please change page number and continue?"})

    else:
        return JsonResponse({'success': "Please create customer profile because cell number does not belong to any customer."})


def Cell_PageExistAJX(request):
    cell = request.GET.get('cell')
    page = request.GET.get('page')
    cellExist = User.objects.filter(cell=cell)
    pageExist = AdvanceMotorcycle.objects.filter(page=page)
    if pageExist:
        return JsonResponse({'page': "page"})
    elif cellExist:
        return JsonResponse({'cell': "cell"})
    else:
        return JsonResponse({'cell_page': "not_exist_cell_page"})
