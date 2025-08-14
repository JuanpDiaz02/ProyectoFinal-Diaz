from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profiles/avatars/', blank=True, null=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.user.username
