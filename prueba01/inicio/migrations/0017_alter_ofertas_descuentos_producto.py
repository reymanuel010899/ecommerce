# Generated by Django 4.1.4 on 2023-02-04 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0016_alter_electronicomodel_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ofertas_descuentos',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oferta_devolver', to='inicio.electronicomodel'),
        ),
    ]
