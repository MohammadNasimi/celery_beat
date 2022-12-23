from django.db import models

# import abstractuser
from django.contrib.auth.models import AbstractUser,UserManager
from django.contrib.auth.hashers import make_password
from django.apps import apps


class Myusermanager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        username = extra_fields['phone']
        return self._create_user(username, email, password, **extra_fields)

class User(AbstractUser):
   phone = models.CharField( max_length=11,null =True,blank=True,unique=True)
   created = models.DateTimeField(auto_now_add=True)

   USERNAME_FIELD = 'phone'

   objects =Myusermanager()
   
   



