from api.models import Station, Train, Stopover, Remark, Composition
from rest_framework import viewsets
import django_filters.rest_framework
from api.serializers import StationSerializer, TrainSerializer, StopoverSerializer, RemarkSerializer, CompositionSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

# Create your views here.

@method_decorator(cache_control(public=True, max_age=60*60*12), name='dispatch')
class StationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows stations to be viewed or edited.
    """
    queryset = Station.objects.all().order_by('eva_number')
    serializer_class = StationSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['usage','eva_number']

class TrainViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows trains to be viewed or edited.
    """
    queryset = Train.objects.all()
    serializer_class = TrainSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['cancelled', 'date','journey_id']


class StopoverViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows stopovers to be viewed or edited.
    """
    queryset = Stopover.objects.all()
    serializer_class = StopoverSerializer
    filterset_fields = ['train']


class RemarkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows remarks to be viewed or edited.
    """
    queryset = Remark.objects.all()
    serializer_class = RemarkSerializer
    filterset_fields = ['train']

class CompositionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Compositions to be viewed or edited.
    """
    queryset = Composition.objects.all()
    serializer_class = CompositionSerializer
    filterset_fields = ['train']
