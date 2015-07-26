from django.db import models
from django.contrib.auth.models import User

class ImprovedUser(User):
    profile_photo = models.ImageField(upload_to="profile_photos")
    def __str__(self):
        return self.username

# Create your models here.
