import random
import string

from django.db import models
from django.utils import timezone

random = ''.join([random.choice(string.ascii_letters+string.digits) for n in range(8)])


# TODO: Create User Model and  required Functions
class User(models.Model):
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)
    gender = models.CharField(max_length=10)
    dob = models.CharField(max_length=20)
    verified = models.BooleanField(default=False)
    token = models.CharField(max_length=8, default=random)
    created_at = models.DateTimeField(default=timezone.now())
    activated_at = models.DateTimeField(blank=True, null=True)

    def activate(self):
        self.verified = True
        self.activated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.email
