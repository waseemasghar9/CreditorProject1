from django.db import models


class Language(models.Model):
    name=models.CharField(max_length=10,blank=True)
    cell= models.CharField(max_length=5, primary_key=True)
    date = models.DateField(null=True)

    father = models.CharField(max_length=20, null=True)

    address = models.TextField(default=True, null=True)


class Framework(models.Model):

    advance=models.CharField(max_length=10)
    cell=models.ForeignKey(to='Language', on_delete=models.CASCADE, related_name='frame')
    page=models.IntegerField(primary_key=True)
    date = models.DateField(null=True)

    # cell = models.CharField(max_length=15)
    bmodel = models.CharField(max_length=8, null=True)
    decidedrate = models.IntegerField(null=True)


class  Country(models.Model):
    page=models.ForeignKey(to='Framework',on_delete=models.CASCADE,related_name='country')
    amount= models.IntegerField(null=True)

    date = models.DateField(null=True)
