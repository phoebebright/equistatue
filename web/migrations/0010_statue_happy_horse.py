# Generated by Django 3.2.16 on 2023-02-21 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_statue_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='statue',
            name='happy_horse',
            field=models.IntegerField(default=0, help_text='1 Yes, -1 No, 0 Unscored'),
        ),
    ]