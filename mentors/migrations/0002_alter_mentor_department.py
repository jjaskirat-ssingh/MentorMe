# Generated by Django 4.0.3 on 2022-03-06 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='department',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
