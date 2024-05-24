# Generated by Django 5.0.6 on 2024-05-24 07:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Channels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'channel',
                'verbose_name_plural': 'channels',
                'db_table': 'channel',
            },
        ),
        migrations.CreateModel(
            name='UserChannel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('video', models.SmallIntegerField()),
                ('followers', models.SmallIntegerField()),
                ('views', models.SmallIntegerField()),
                ('comment', models.SmallIntegerField()),
                ('country', models.CharField(max_length=100)),
                ('created_date', models.DateField()),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.channels')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_channel',
            },
        ),
    ]
