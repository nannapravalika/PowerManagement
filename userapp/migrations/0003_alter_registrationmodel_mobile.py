# Generated by Django 4.0.1 on 2022-02-21 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_remove_newconnectionmodel_usc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationmodel',
            name='mobile',
            field=models.BigIntegerField(),
        ),
    ]
