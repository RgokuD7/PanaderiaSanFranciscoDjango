# Generated by Django 4.2.1 on 2023-07-01 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0012_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default='static/core/img/logo.jpg', upload_to='administracion/media/img/productos', verbose_name='Imagen del Producto'),
        ),
    ]
