# Generated by Django 4.2.11 on 2024-11-22 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_rename_value_client_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
