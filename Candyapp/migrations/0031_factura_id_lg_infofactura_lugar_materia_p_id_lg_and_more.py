# Generated by Django 4.0.3 on 2022-05-05 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Candyapp', '0030_lugar'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='id_lg',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Candyapp.lugar', verbose_name='Lugar'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='infofactura',
            name='lugar',
            field=models.CharField(default=1, max_length=50, verbose_name='Lugar'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='materia_p',
            name='id_lg',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Candyapp.lugar', verbose_name='Lugar'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='id_lg',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Candyapp.lugar', verbose_name='Lugar'),
            preserve_default=False,
        ),
    ]
