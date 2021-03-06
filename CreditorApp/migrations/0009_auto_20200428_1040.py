# Generated by Django 3.0.5 on 2020-04-28 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CreditorApp', '0008_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[('OWNER', 1), ('MEMBER', 3), ('ADMIN', 2)], null=True),
        ),
    ]
