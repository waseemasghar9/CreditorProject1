from django.db import models

from CreditorApp.models import usermodel


class AdvanceMotorcycle(models.Model):
    date = models.DateField(null=True)
    page = models.CharField(max_length=5, primary_key=True,)
   # cell = models.CharField(max_length=15)
    bmodel = models.CharField(max_length=8)
    decidedrate = models.IntegerField(null=True)
    advance = models.IntegerField(null=True)
    cell=models.ForeignKey(to='User', on_delete=models.CASCADE,related_name='adv')
    month= models.IntegerField(null=True)
    day = models.IntegerField(null=True)


