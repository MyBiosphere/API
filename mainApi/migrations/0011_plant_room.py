# Generated by Django 4.0.2 on 2022-06-20 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApi', '0010_sensorsbox_housemetrics'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='room',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]