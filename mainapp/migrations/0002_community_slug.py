# Generated by Django 2.0.4 on 2018-05-06 14:10

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='aw', editable=False, populate_from=models.CharField(max_length=300)),
            preserve_default=False,
        ),
    ]
