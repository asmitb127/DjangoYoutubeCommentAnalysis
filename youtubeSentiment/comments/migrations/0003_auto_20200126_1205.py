# Generated by Django 3.0.2 on 2020-01-26 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20200126_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='channel',
            name='channel_name',
            field=models.TextField(),
        ),
    ]