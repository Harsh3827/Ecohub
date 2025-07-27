from django.db import models

# Create your models here.

class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()
    category = models.CharField(max_length=50, default='General')
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', 'question']
    
    def __str__(self):
        return self.question
