# Generated by Django 4.1.4 on 2023-03-16 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carro_compra', '0008_remove_carro_compras_moda'),
        ('inicio', '0033_rename_categori_ropamodels_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='electronicomodel',
            name='size',
            field=models.CharField(blank=True, choices=[('1', 'L'), ('2', 'M'), ('3', 'X'), ('4', 'XL')], max_length=1),
        ),
        migrations.DeleteModel(
            name='RopaModels',
        ),
    ]
