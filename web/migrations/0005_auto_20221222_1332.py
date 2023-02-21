# Generated by Django 3.2.16 on 2022-12-22 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_statue_servant_partner'),
    ]

    operations = [
        migrations.AddField(
            model_name='statue',
            name='other_img_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='statue',
            name='details_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
