from django.db import models


class InstallmentModel(models.Model):
    page= models.ForeignKey(to='AdvanceMotorcycle',on_delete=models.CASCADE,related_name='inst')
    date = models.DateField(null=True)
    amount = models.IntegerField(null=True)
    discount= models.IntegerField(null=True)
    fine= models.IntegerField(null=True)
