# Generated by Django 2.2.1 on 2019-05-22 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a', '0004_auto_20190518_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='IP',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='host',
            name='hostname',
            field=models.CharField(max_length=32),
        ),
    ]
