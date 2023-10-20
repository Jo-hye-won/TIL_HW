# Generated by Django 4.2.6 on 2023-10-20 03:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0002_board_like_users_board_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='hate_users',
            field=models.ManyToManyField(related_name='hate_articles', to=settings.AUTH_USER_MODEL),
        ),
    ]