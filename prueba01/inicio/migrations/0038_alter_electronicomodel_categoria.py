# Generated by Django 4.1.4 on 2023-03-18 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0037_electronicomodel_tipa_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electronicomodel',
            name='categoria',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='categorias', to='inicio.categoria'),
        ),
    ]
