# Generated by Django 4.1.4 on 2023-03-14 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0020_electronicomodel_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='ofertas_descuentos',
            name='porciento',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
