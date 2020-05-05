from django.http import JsonResponse

from CreditorApp.models import User


def usernamecheck(request):
    cell = request.GET.get('cell')
    cellexist = User.objects.filter(cell=cell).exists()
    if not cellexist:
        return JsonResponse({'success': ""})
    else:
        return JsonResponse({'success': "Cell number is already exist."})