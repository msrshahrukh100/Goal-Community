# Generated by Django 2.0.4 on 2018-05-07 02:48

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20180506_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name'),
        ),
    ]
