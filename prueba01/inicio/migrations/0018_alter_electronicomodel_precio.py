# Generated by Django 4.1.4 on 2023-02-04 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0017_alter_ofertas_descuentos_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electronicomodel',
            name='precio',
            field=models.IntegerField(),
        ),
    ]
