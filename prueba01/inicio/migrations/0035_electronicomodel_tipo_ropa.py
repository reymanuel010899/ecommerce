# Generated by Django 4.1.4 on 2023-03-17 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0034_electronicomodel_size_delete_ropamodels'),
    ]

    operations = [
        migrations.AddField(
            model_name='electronicomodel',
            name='tipo_ropa',
            field=models.CharField(blank=True, choices=[('1', 'abrigo'), ('2', 'pantalon'), ('3', 'tenis')], max_length=1),
        ),
    ]