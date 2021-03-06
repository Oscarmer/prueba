# Generated by Django 4.0.3 on 2022-05-06 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Candyapp', '0037_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia_p',
            name='contacto',
            field=models.CharField(max_length=14, null=True, verbose_name='contacto'),
        ),
        migrations.AlterField(
            model_name='materia_p',
            name='descripcion',
            field=models.TextField(max_length=100, null=True, verbose_name='descripcion'),
        ),
        migrations.AlterField(
            model_name='materia_p',
            name='mincant',
            field=models.IntegerField(null=True, verbose_name='cantidad minima'),
        ),
        migrations.AlterField(
            model_name='materia_p',
            name='tiempo',
            field=models.CharField(max_length=14, null=True, verbose_name='tiempo de entrega'),
        ),
    ]
