from django.db import models
from django.utils.timezone import now


class Race(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    created = models.DateTimeField(default=now,auto_now=False)
    image = models.ImageField(null=True, max_length=400,upload_to='images/races')

    def get_image_url(self):
        return self.image.url

    def __str__(self):
        return self.name


class Pilot(models.Model):
    name = models.CharField(max_length=200)
    bike_name = models.CharField(max_length=200)
    engine_size = models.IntegerField()
    created = models.DateTimeField(default=now, auto_now=False)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['race', 'bike_name'], name='name of constraint')
        ]

    def __str__(self):
        return self.name