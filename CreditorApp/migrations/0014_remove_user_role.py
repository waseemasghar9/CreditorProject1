# Generated by Django 3.0.5 on 2020-04-28 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CreditorApp', '0013_auto_20200428_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
    ]
