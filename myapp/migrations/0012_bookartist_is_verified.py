# Generated by Django 3.2 on 2021-04-21 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_bookartist_artist_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookartist',
            name='is_verified',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
