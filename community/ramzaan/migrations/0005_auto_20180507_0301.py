# Generated by Django 2.0.4 on 2018-05-07 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ramzaan', '0004_auto_20180507_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ramzaangroup',
            name='height_field',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ramzaangroup',
            name='width_field',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]