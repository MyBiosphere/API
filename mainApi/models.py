from django.db import models

# Create your models here.


class Sickness(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()


class Plant(models.Model):
    STATUS = (
        ('healthy', 'This plant is healthy'),
        ('sick', 'This plant is sick'),
        ('dry', 'This plant is dry'),
        ('drown', 'This plant is drown'),
    )

    name = models.CharField(max_length=120)
    description = models.TextField()
    status = models.CharField(
        max_length=32,
        choices=STATUS,
        default='Healthy',
    )
    sickness = models.ForeignKey(Sickness, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name



