# Generated by Django 4.1.4 on 2023-03-18 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0036_alter_electronicomodel_tipo_ropa'),
    ]

    operations = [
        migrations.AddField(
            model_name='electronicomodel',
            name='tipa_genero',
            field=models.CharField(blank=True, choices=[('2', 'mujer'), ('3', 'niño')], max_length=1),
        ),
    ]
