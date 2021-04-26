# Generated by Django 3.1.7 on 2021-03-26 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='gameStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rank', models.CharField(max_length=250)),
                ('Map', models.CharField(max_length=250)),
                ('ScoreAtHalf', models.CharField(max_length=250)),
                ('FinalScore', models.CharField(max_length=250)),
                ('Kills', models.IntegerField(default=0)),
                ('Deaths', models.IntegerField(default=0)),
                ('Assists', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('userNameText', models.CharField(max_length=250)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
            ],
        ),
    ]
