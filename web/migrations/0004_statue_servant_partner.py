# Generated by Django 3.2.16 on 2022-12-21 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_statue_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='statue',
            name='servant_partner',
            field=models.IntegerField(default=99),
        ),
    ]
