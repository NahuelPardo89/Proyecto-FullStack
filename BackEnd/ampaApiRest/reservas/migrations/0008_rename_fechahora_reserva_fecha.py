# Generated by Django 4.2.1 on 2023-06-14 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0007_reserva_costo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserva',
            old_name='fechaHora',
            new_name='fecha',
        ),
    ]