# Generated by Django 4.0.3 on 2022-04-30 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Candyapp', '0026_entregado_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candycarrito',
            name='precio',
            field=models.IntegerField(null=True, verbose_name='precio'),
        ),
        migrations.AlterField(
            model_name='infofactura',
            name='id_ft',
            field=models.IntegerField(verbose_name='factura'),
        ),
    ]
