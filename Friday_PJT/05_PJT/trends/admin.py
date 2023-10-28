from django.contrib import admin
from .models import Keyword, Trend


# Register your models here.
admin.site.register([Keyword,Trend])
# admin.site.register(Trend)
