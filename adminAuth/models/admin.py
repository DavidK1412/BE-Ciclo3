from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    #Crea un usuario
    def create_user(self, username, password = None):
        if not username:
            raise ValueError('Se debe dar un usuario!')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_admin(self, username, password):
        user = self.create_user(username= username, password= password)
        user.is_admin = True
        user.save(using = self.db)
        return user

class Admin(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key= True)
    username = models.CharField('Username', max_length=20, unique=True)
    password = models.CharField('Password', max_length=256)
    email = models.EmailField('Email', max_length=120)
    nombre = models.CharField('Nombre', max_length=35)

    def save(self, **kwargs):
        hashing = 'mUosa029Drso4wpI6mxN90'
        self.password = make_password(self.password, hashing)
        super().save(**kwargs)
    
    objects = UserManager()
    USERNAME_FIELD = 'username'
