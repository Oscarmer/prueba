# Generated by Django 4.0.3 on 2022-04-18 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Candyapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='materia_s',
            fields=[
                ('id_ms', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20, verbose_name='nombre_ms')),
                ('descripcion', models.TextField(max_length=100, verbose_name='descripcion_ms')),
                ('estado', models.BooleanField(verbose_name='estado_ms')),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(max_length=100, verbose_name='descripcion'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='variaciones',
            field=models.IntegerField(verbose_name='variaciones'),
        ),
    ]
