from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # created_at = models.DateField
    # created_at = models.TimeField
    updated_at = models.DateTimeField(auto_now=True)