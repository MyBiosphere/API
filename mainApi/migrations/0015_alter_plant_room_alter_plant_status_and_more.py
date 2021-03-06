# Generated by Django 4.0.2 on 2022-06-21 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApi', '0014_remove_plant_blooming_duration_remove_plant_sickness_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='room',
            field=models.CharField(choices=[('living', 'Salon'), ('bedroom', 'Chambre'), ('kitchen', 'Cuisine'), ('study', 'Bureau'), ('bathroom', 'Salle de bain'), ('balcony', 'Balcon'), ('terrace', 'Terrasse')], default='living', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='status',
            field=models.CharField(choices=[('healthy', 'Cette plante est en bonne santée.'), ('sick', 'Cette plante est malade.'), ('dry', 'Cette plante est asséchée.'), ('drown', 'Cette plante est trop arrosée.')], default='Healthy', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='sunshine',
            field=models.CharField(choices=[('directSunlight', 'Lumière directe'), ('indirectSunlight', 'Lumière indirecte'), ('shady', 'Ombragé')], default='directSunlight', max_length=120, null=True),
        ),
    ]
