# Generated by Django 4.2.1 on 2023-05-31 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_carritoproductos_detallecarritoproductos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carritoproductos',
            name='monto',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='detallecarritoproductos',
            name='monto',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]
