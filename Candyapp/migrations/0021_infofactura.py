# Generated by Django 4.0.3 on 2022-04-27 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Candyapp', '0020_entregado_descripcion_alter_entregado_id_cr'),
    ]

    operations = [
        migrations.CreateModel(
            name='infofactura',
            fields=[
                ('id_if', models.AutoField(primary_key=True, serialize=False)),
                ('precio', models.IntegerField(verbose_name='precio')),
                ('id_eg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Candyapp.entregado', verbose_name='entregado')),
                ('id_ft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Candyapp.factura', verbose_name='factura')),
            ],
        ),
    ]
