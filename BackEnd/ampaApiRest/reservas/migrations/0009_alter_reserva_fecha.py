# Generated by Django 4.2.1 on 2023-06-14 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0008_rename_fechahora_reserva_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='fecha',
            field=models.DateField(),
        ),
    ]
