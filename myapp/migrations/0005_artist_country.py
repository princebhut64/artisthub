# Generated by Django 3.2 on 2021-04-14 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_artist_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='country',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]