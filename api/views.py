from api.models import Station, Line, Operator, Train, Stopover, Remark, Composition
from rest_framework import viewsets
import django_filters.rest_framework
from api.serializers import StationSerializer, LineSerializer, OperatorSerializer ,TrainSerializer, StopoverSerializer, RemarkSerializer, CompositionSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control

# Create your views here.

@method_decorator(cache_control(public=True, max_age=60*60*12), name='dispatch')
class StationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows stations to be viewed or edited.
    """
    queryset = Station.objects.all().order_by('id')
    serializer_class = StationSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['eva_number', 'name']

class LineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows lines to be viewed or edited.
    """
    queryset = Line.objects.all().order_by('id')
    serializer_class = LineSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['product', 'operator','number']

class OperatorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that operators to be viewed or edited.
    """
    queryset = Operator.objects.all().order_by('id')
    serializer_class = OperatorSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name']

class TrainViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows trains to be viewed or edited.
    """
    queryset = Train.objects.all().order_by('id')
    serializer_class = TrainSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['cancelled', 'date','trip_id', 'line']


class StopoverViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows stopovers to be viewed or edited.
    """
    queryset = Stopover.objects.all().order_by('id')
    serializer_class = StopoverSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['train','stop_index']


class RemarkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows remarks to be viewed or edited.
    """
    queryset = Remark.objects.all().order_by('id')
    serializer_class = RemarkSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['train','message']

class CompositionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Compositions to be viewed or edited.
    """
    queryset = Composition.objects.all().order_by('id')
    serializer_class = CompositionSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['train']
