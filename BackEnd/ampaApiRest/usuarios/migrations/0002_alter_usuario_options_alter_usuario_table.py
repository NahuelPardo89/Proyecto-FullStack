# Generated by Django 4.2.1 on 2023-06-01 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
        migrations.AlterModelTable(
            name='usuario',
            table='Usuario',
        ),
    ]
