# Generated by Django 5.0.6 on 2024-07-22 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0007_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='../media/producto_images/'),
        ),
    ]