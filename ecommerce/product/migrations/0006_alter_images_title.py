# Generated by Django 3.2.5 on 2021-10-30 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
