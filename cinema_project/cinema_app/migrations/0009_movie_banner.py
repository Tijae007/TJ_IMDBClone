# Generated by Django 3.1.1 on 2021-03-31 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0008_movie_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='banner',
            field=models.FileField(default=1, upload_to='movies_banner'),
            preserve_default=False,
        ),
    ]
