from django.db import models

# Create your models here.
class Article(models.Model):
    name = models.TextField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,  decimal_places=1)
    is_published = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
