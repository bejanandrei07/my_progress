# Generated by Django 4.2.21 on 2025-05-27 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('body_data', '0003_measurements_age_measurements_height'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurements',
            name='biceps',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='measurements',
            name='calves',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='measurements',
            name='chest',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='measurements',
            name='hips',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='measurements',
            name='sholders',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='measurements',
            name='thigs',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='measurements',
            name='triceps',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='measurements',
            name='waist',
            field=models.FloatField(default=0),
        ),
    ]
