# Generated by Django 3.2.16 on 2023-02-21 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_auto_20230221_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='statue',
            name='updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
