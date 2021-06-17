# Generated by Django 3.2 on 2021-04-16 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=200)),
                ('photos', models.FileField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
