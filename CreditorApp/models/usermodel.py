from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,  cell,name,father,address,date, password):
        if not cell:
            raise ValueError('Users must have cell number')

        user = self.model(
            date=date,
            cell=cell,
            name=name,
            father= father,
            address=address,
            password=password,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name,father,address, cell,date, password):
        user = self.create_user(
            cell=cell,
            date=date,
            name=name,
            father=father,
            address=address,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser,PermissionsMixin):


    date = models.DateField(null=True)
    name = models.CharField(max_length=20, null=True)
    father = models.CharField(max_length=20, null=True)
    cell = models.CharField(max_length=15, primary_key=True)
    address = models.TextField(default=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_member= models.BooleanField(null=True)
    is_owner = models.BooleanField(null=True)

    class Meta:
        permissions = (
            ("can_drive", "Can drive"),
            ("can_vote", "Can vote in elections"),
            ("can_drink", "Can drink alcohol"),
        )

    objects = UserManager()

    USERNAME_FIELD = 'cell'
    REQUIRED_FIELDS = ['date','name','father','address']

    @property
    def is_staff(self):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    def has_perm(self, perm, obj=None):
        return True


    def __str__(self):
        return (self.name)