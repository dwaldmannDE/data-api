from api.models import Station, Train, Stopover, Remark
from rest_framework import serializers


class StationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Station
        fields = ['eva_number', 'name', 'usage', 'lng', 'lat']


class TrainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Train
        fields = ['line', 'number', 'type', 'operator', 'date', 'cancelled', 'journey_id', 'origin', 'destination']

class StopoverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stopover
        fields = ['station_id', 'stop_index', 'train_id', 'platform', 'departure_time', 'departure_scheduled_time', 'arrival_time', 'arrival_scheduled_time']

class RemarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Remark
        fields = ['train_id', 'message']

class CompositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Remark
        fields = ['train_id', 'message']