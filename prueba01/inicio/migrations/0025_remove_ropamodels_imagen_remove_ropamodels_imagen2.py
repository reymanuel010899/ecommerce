# Generated by Django 4.1.4 on 2023-03-16 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0024_ropamodels_imagen_ropamodels_imagen2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ropamodels',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='ropamodels',
            name='imagen2',
        ),
    ]
