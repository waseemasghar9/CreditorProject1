# Generated by Django 3.0.5 on 2020-04-17 17:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CreditorApp', '0003_auto_20200417_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advancemotorcycle',
            name='cell',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='installmentmodel',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreditorApp.AdvanceMotorcycle'),
        ),
    ]
