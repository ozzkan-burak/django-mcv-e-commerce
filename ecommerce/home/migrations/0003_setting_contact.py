# Generated by Django 3.2.5 on 2021-10-30 12:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_product_setting'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='contact',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
