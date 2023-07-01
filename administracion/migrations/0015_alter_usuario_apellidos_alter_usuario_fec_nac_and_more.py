# Generated by Django 4.2.1 on 2023-07-01 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0014_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='apellidos',
            field=models.CharField(max_length=50, verbose_name='Apellidos'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fec_nac',
            field=models.DateField(verbose_name='Fecha Nacimiento'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='mail',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombres',
            field=models.CharField(max_length=50, verbose_name='Nombres'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(max_length=15, verbose_name='Password'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rut',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Rut'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.IntegerField(verbose_name='Telefono'),
        ),
    ]