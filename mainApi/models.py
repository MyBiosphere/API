from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Sickness(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()


class Plant(models.Model):
    STATUS = (
        ('healthy', 'Cette plante est en bonne santée.'),
        ('sick', 'Cette plante est malade.'),
        ('dry', 'Cette plante est asséchée.'),
        ('drown', 'Cette plante est trop arrosée.'),
    )

    ROOM = (
        ('living', 'Salon'),
        ('bedroom', 'Chambre'),
        ('kitchen', 'Cuisine'),
        ('study', 'Bureau'),
        ('bathroom', 'Salle de bain'),
        ('balcony', 'Balcon'),
        ('terrace', 'Terrasse'),
    )

    SUNSHINE = (
        ('direct_sunlight', 'Lumière directe'),
        ('indirect_sunlight', 'Lumière indirecte'),
        ('shady', 'Ombragé'),
    )

    name = models.CharField(max_length=120)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    description = models.TextField()

    status = models.CharField(
        max_length=120,
        choices=STATUS,
        default='Healthy',
    )

    room = models.CharField(
        max_length=120,
        choices=ROOM,
        default='living',
    )
    watering = models.IntegerField(blank=True, null=True)
    sunshine = models.CharField(
        max_length=120,
        choices=SUNSHINE,
        default='direct_sunlight',
    )
    repot = models.IntegerField(blank=True, null=True)
    blooming_time = models.CharField(max_length=120, blank=True, null=True)\

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=120)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    description = models.TextField()
    done = models.BooleanField(default=False)
    plant = models.ForeignKey(
        Plant,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    @property
    def plant_name(self):
        return self.plant.name

    @property
    def plant_id(self):
        return self.plant.id


class SensorsBox(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    boxNumber = models.IntegerField(blank=True, null=True)


class HouseMetrics(models.Model):
    box = models.ForeignKey(
        SensorsBox,
        on_delete=models.CASCADE
    )
    co2 = models.IntegerField(blank=True, null=True)
    temperature = models.IntegerField(blank=True, null=True)
    humidity = models.IntegerField(blank=True, null=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    plants = models.ManyToManyField(Plant)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        token = Token.objects.create(user=instance)
        print(token.key)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
