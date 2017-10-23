# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-23 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Denuncia', '0005_auto_20171022_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='denuncia',
            name='herido',
            field=models.CharField(choices=[('AB', 'Abandono en la Calle'), ('EX', 'Exposición a Temperaturas Extremas'), ('FA', 'Falta de Agua'), ('FC', 'Falta de Comida'), ('V', 'Violencia'), ('VA', 'Venta Ambulante')], max_length=50),
        ),
    ]
