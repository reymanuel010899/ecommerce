# Generated by Django 4.1.4 on 2023-01-06 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0008_alter_vistas_articulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electronicomodel',
            name='rating',
            field=models.PositiveIntegerField(blank=True, default=1),
        ),
    ]
