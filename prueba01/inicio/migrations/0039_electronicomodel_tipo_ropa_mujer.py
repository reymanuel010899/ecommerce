# Generated by Django 4.1.4 on 2023-03-18 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0038_alter_electronicomodel_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='electronicomodel',
            name='tipo_ropa_mujer',
            field=models.CharField(blank=True, choices=[('1', 'vestido'), ('2', 'zapatilla'), ('3', 'ropa interior'), ('4', 'blusa')], max_length=1),
        ),
    ]
