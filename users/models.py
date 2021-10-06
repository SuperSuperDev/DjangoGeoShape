from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(_('First Name of User'),
        max_length=40, blank=True)

    last_name = models.CharField(_('Last Name of User'),
        max_length=40, blank=True)

    nickname = models.CharField(_('Nickname of User'),
        max_length=40, blank=True)

