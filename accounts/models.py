from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    # Example field for tracking visits (can be expanded)
    visits = models.IntegerField(default=0)
    last_visit = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.username
