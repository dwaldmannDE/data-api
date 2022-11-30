from django.db import models
from datetime import date
# Create your models here.


class Station(models.Model):

    USAGE = (
        ('FV', 'Fernverkehr'),
        ('RV', 'Regionalverkehr'),
        ('XX', 'Nicht DB'),
    )

    eva_number = models.CharField(max_length=16, unique=True)
    name = models.CharField(max_length=64)
    usage = models.CharField(max_length=2, choices=USAGE, default='XX')
    lng = models.DecimalField(max_digits=9, decimal_places=7)
    lat = models.DecimalField(max_digits=9, decimal_places=7)

    def __str__(self):
        return self.name


class Train(models.Model):

    line = models.CharField(max_length=4)
    number = models.IntegerField()
    type = models.CharField(max_length=8)
    operator = models.CharField(max_length=32)
    date = models.DateField(default=date.today)
    cancelled = models.BooleanField(default=False)
    journey_id = models.CharField(max_length=16)
    origin = models.OneToOneField(
        Station, on_delete=models.CASCADE, related_name='train_origin')
    destination = models.OneToOneField(
        Station, on_delete=models.CASCADE, related_name='train_destination')

    def __str__(self):
        return '{} {}'.format(self.type, self.number)


class Remark(models.Model):

    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    message = models.CharField(max_length=256)


class Stopover(models.Model):

    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    stop_index = models.IntegerField()
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    platform = models.CharField(max_length=32, blank=True, null=True)
    departure_time = models.DateTimeField(blank=True, null=True)
    departure_scheduled_time = models.DateTimeField(blank=True, null=True)
    arrival_time = models.DateTimeField(blank=True, null=True)
    arrival_scheduled_time = models.DateTimeField(blank=True, null=True)