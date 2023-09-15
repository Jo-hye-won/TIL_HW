from django.db import models

# Create your models here.
class Garage(models.Model):
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()
    is_parking_available = models.BooleanField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()

'''
pip install ipython
python manage.py shell_plus
In [1] : garages = Garage.objects.all()
In [2] : garage = Garage()
In [3] : garage.location = '서울'
In [4] : garage.capacity = 30
In [5] : garage.is_parking_available = False
In [6] : garage.opening_time = '08:00:00'
In [7] : garage.closing_time = '22:00:00'
In [8] : garage.save()

In [9] : garage = Garage.objects.all()
In [10] : garage2 = Garage()
In [11] : garage2.location = '부산'
In [12] : garage2.capacity = 20
In [13] : garage2.is_parking_available = True
In [14] : garage2.opening_time = '07:00:00'
In [15] : garage2.closing_time = '23:00:00'
In [16] : garage2.save()

'''
