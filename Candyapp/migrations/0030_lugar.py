# Generated by Django 4.0.3 on 2022-05-05 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Candyapp', '0029_alter_infofactura_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='lugar',
            fields=[
                ('id_lg', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Lugar')),
            ],
        ),
    ]
