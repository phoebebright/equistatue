# Generated by Django 4.1.6 on 2023-03-03 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_statue_like_dontknow_statue_like_no_statue_like_yes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statue',
            name='servant_partner',
        ),
        migrations.AddField(
            model_name='statue',
            name='servant_partner_avg',
            field=models.FloatField(default=0),
        ),
    ]