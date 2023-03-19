# Generated by Django 4.1.4 on 2023-01-29 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0011_electronicomodel_cantidad'),
        ('carro_compra', '0002_carro_compras'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='carro_compras',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='carro_compras',
            name='productos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carro_devolver', to='inicio.electronicomodel'),
        ),
        migrations.DeleteModel(
            name='card_shop',
        ),
    ]
