# Generated by Django 4.1.4 on 2023-03-16 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0029_remove_ropamodels_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='ropamodels',
            name='precio',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
