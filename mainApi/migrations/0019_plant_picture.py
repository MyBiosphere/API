# Generated by Django 4.0.2 on 2022-06-23 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApi', '0018_alter_plant_status_alter_plant_sunshine'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='plants'),
        ),
    ]
