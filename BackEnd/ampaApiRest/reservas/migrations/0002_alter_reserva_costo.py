# Generated by Django 4.2.1 on 2023-06-02 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instalaciones', '0001_initial'),
        ('reservas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='costo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='costo_reserva_usuario', to='instalaciones.instalaciones'),
        ),
    ]
