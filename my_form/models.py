from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Custom User Model
class CustomUser(AbstractUser):
    # Add any additional fields here
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username

# Profile Model
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    state = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.user.username