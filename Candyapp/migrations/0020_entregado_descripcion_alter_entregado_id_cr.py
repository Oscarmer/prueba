# Generated by Django 4.0.3 on 2022-04-25 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Candyapp', '0019_rename_entegado_entregado'),
    ]

    operations = [
        migrations.AddField(
            model_name='entregado',
            name='descripcion',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='entregado',
            name='id_cr',
            field=models.CharField(max_length=50, verbose_name='carrito'),
        ),
    ]