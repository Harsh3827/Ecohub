from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Tip(models.Model):
    CATEGORY_CHOICES = [
        ('energy', 'Renewable Energy'),
        ('lifestyle', 'Green Lifestyle'),
        ('tech', 'Eco Technology'),
        ('news', 'Sustainability News'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    file_upload = models.FileField(upload_to='tip_uploads/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tip-detail', kwargs={'pk': self.pk})
