from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from rest_framework.authtoken.models import Token as DefaultTokenModel

from .utils import import_callable


class User(AbstractUser):
    avatar = models.ImageField(upload_to='', null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)


TokenModel = import_callable(
    getattr(settings, 'REST_AUTH_TOKEN_MODEL', DefaultTokenModel))