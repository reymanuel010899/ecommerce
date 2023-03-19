# Generated by Django 4.1.4 on 2023-02-01 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0013_ofertas_descuentos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ofertas_descuentos',
            name='producto',
        ),
        migrations.AddField(
            model_name='ofertas_descuentos',
            name='producto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inicio.electronicomodel'),
            preserve_default=False,
        ),
    ]
