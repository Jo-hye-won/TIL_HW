# Generated by Django 4.2.5 on 2023-09-14 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_alter_article_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='price',
            field=models.DecimalField(decimal_places=1, max_digits=10),
        ),
    ]