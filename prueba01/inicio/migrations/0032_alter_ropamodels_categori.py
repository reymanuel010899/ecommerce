# Generated by Django 4.1.4 on 2023-03-16 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0031_ropamodels_cantidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ropamodels',
            name='categori',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ropa_devolver', to='inicio.categoria'),
        ),
    ]