# Generated by Django 4.2.21 on 2025-05-26 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('body_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurements',
            name='weight',
            field=models.FloatField(default=0),
        ),
    ]
