# Generated by Django 3.0.2 on 2020-01-26 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_name', models.TextField(unique=True)),
                ('channel_id', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('accessed_date', models.DateTimeField(auto_now_add=True)),
                ('likes', models.IntegerField()),
                ('dislikes', models.IntegerField()),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comments.Channel')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comments.Author')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comments.Videos')),
            ],
        ),
    ]