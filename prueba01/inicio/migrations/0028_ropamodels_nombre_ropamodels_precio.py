# Generated by Django 4.1.4 on 2023-03-16 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0027_remove_vistas_imagen_remove_vistas_imagen2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ropamodels',
            name='nombre',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ropamodels',
            name='precio',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]