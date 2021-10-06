import uuid, random
from django.db import models
from django.contrib.auth.models import AbstractUser

def random_string():
    return str(random.randint(10000, 99999))

class User(AbstractUser):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    user_image = models.CharField(
        max_length=250, 
        default=f'https://avatars.dicebear.com/api/avataaars/{random_string}.svg?size=150' 
        )
    bio = models.TextField(max_length=500, blank=True)
    dark_mode = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.username)