import uuid
from django.db import models
from django.utils import timezone
# Create your models here.


class Station(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    eva_number = models.IntegerField()
    name = models.CharField(max_length=64)
    lng = models.DecimalField(max_digits=9, decimal_places=7)
    lat = models.DecimalField(max_digits=9, decimal_places=7)
    query = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Operator(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Line(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    product = models.CharField(max_length=255)
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Train(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    cancelled = models.BooleanField(default=False)
    trip_id = models.CharField(max_length=64)
    origin = models.ForeignKey(
        Station, on_delete=models.CASCADE, related_name='train_origin')
    destination = models.ForeignKey(
        Station, on_delete=models.CASCADE, related_name='train_destination')

    def __str__(self):
        return '{} - {}'.format(self.name, self.date)


class Remark(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    message = models.CharField(max_length=1024)

    def __str__(self):
        return '{}'.format(self.message)


class Stopover(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    stop_index = models.IntegerField()
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    platform = models.CharField(max_length=32, blank=True, null=True)
    departure_planned_time = models.DateTimeField(blank=True, null=True)
    departure_actual_time = models.DateTimeField(blank=True, null=True)
    arrival_planned_time = models.DateTimeField(blank=True, null=True)
    arrival_actual_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.stop_index)

class Composition(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    coach_sequence = models.JSONField()
