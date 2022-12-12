from api.models import Station, Operator, Line, Train, Stopover, Remark, Composition
from rest_framework import serializers


class StationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Station
        fields = ['id', 'eva_number','name', 'lng', 'lat', 'query', 'url']


class OperatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Operator
        fields = ['id', 'name', 'url']


class LineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Line
        fields = ['id', 'number', 'name', 'product', 'operator', 'url']


class TrainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Train
        fields = ['id', 'name', 'line', 'date', 'cancelled',
                  'trip_id', 'origin', 'destination', 'url']


class StopoverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stopover
        fields = ['id', 'station', 'stop_index', 'train', 'platform', 'departure_planned_time',
                  'departure_actual_time', 'arrival_planned_time', 'arrival_actual_time', 'url']


class RemarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Remark
        fields = ['id', 'train', 'message', 'url']


class CompositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Composition
        fields = ['id', 'train', 'coach_sequence', 'url']
