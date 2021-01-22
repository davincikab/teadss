from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_farmer = models.BooleanField(default=False)
    is_decisonmaker = models.BooleanField(default=False)
    phone_number = models.CharField("Phone Number", max_length=13, null=True)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

