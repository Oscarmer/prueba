# Generated by Django 4.0.3 on 2022-04-25 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Candyapp', '0017_delete_entegado'),
    ]

    operations = [
        migrations.CreateModel(
            name='entegado',
            fields=[
                ('id_eg', models.AutoField(primary_key=True, serialize=False)),
                ('mesa', models.CharField(max_length=50)),
                ('cliente', models.CharField(max_length=50, null=True)),
                ('id_cr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Candyapp.candycarrito', verbose_name='carrito')),
            ],
        ),
    ]
