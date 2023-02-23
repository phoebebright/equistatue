# Generated by Django 4.1.6 on 2023-02-23 21:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0012_statue_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statue',
            name='happy_horse',
        ),
        migrations.AddField(
            model_name='statue',
            name='missing_image',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True)),
                ('score', models.SmallIntegerField(default=0, help_text="-1 for dislike, 1 for like, 0 for don't know")),
                ('comments', models.TextField(blank=True, null=True)),
                ('creator', models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('statue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.statue')),
            ],
        ),
    ]
