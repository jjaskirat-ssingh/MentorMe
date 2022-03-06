# Generated by Django 4.0.3 on 2022-03-06 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='department',
            field=models.CharField(default='CSED', max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='interests',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]