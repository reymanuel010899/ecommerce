# Generated by Django 4.1.4 on 2023-02-04 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carro_compra', '0003_alter_carro_compras_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro_compras',
            name='cantidad',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
