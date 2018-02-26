# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=400)),
                ('URL', models.URLField()),
                ('UploadDate', models.DateField()),
                ('ReleasedDate', models.DateField()),
                ('Rating', models.FloatField(default=0)),
                ('Comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=400, unique=True)),
                ('Featuring', models.CharField(max_length=400)),
                ('isBand', models.BooleanField(default=False)),
                ('Member', models.CharField(max_length=4000)),
                ('Rating', models.FloatField()),
                ('Comment', models.TextField()),
                ('PersonalWebsite', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemID', models.IntegerField(default=0, unique=True)),
                ('Title', models.CharField(max_length=400)),
                ('URL', models.URLField()),
                ('UploadDate', models.DateField()),
                ('ReleasedDate', models.DateField()),
                ('Rating', models.FloatField(default=0)),
                ('Comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=400, unique=True)),
                ('Featuring', models.CharField(max_length=400)),
                ('isBand', models.BooleanField(default=False)),
                ('Member', models.CharField(max_length=4000)),
                ('Rating', models.FloatField()),
                ('Comment', models.TextField()),
                ('PersonalWebsite', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlayList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PlayListName', models.CharField(max_length=400)),
                ('UserID', models.IntegerField()),
                ('CreatedDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemID', models.IntegerField()),
                ('RatingType', models.CharField(max_length=128)),
                ('UserID', models.IntegerField()),
                ('RatingDate', models.DateField()),
                ('RatingValue', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(

            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(null=True, upload_to='profile_pictures/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('Title', models.CharField(max_length=200)),
                ('URL', models.URLField()),
                ('ReleasedDate', models.DateField()),
                ('Genre', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='musicapp.Genre')),
                ('Rating', models.FloatField(default=0)),
                ('Comment', models.TextField(default='')),
                ('Artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.Artist')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='Artist',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='musicapp.Artist'),
        ),
        migrations.AddField(
            model_name='album',
            name='Genre',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='musicapp.Genre'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='Song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.Song'),
        ),
        migrations.AddField(
            model_name='album',
            name='Song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.Song'),
        ),
    ]
