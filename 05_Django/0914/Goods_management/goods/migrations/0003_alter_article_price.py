# Generated by Django 4.2.5 on 2023-09-14 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_article_created_at_article_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
