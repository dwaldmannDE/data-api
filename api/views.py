from api.models import Station, Train, Stopover, Remark
from rest_framework import viewsets, generics
import django_filters.rest_framework
from api.serializers import StationSerializer, TrainSerializer, StopoverSerializer, RemarkSerializer


# Create your views here.

class StationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows stations to be viewed or edited.
    """
    queryset = Station.objects.all().order_by('eva_number')
    serializer_class = StationSerializer
    permission_classes = []
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['usage','eva_number']

class StationListView(generics.ListAPIView):
    """
    API endpoint that allows stations to be listed.
    """
    queryset = Station.objects.all().order_by('eva_number')
    serializer_class = StationSerializer
    permission_classes = []
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['usage']

class TrainViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows trains to be viewed or edited.
    """
    queryset = Train.objects.all()
    serializer_class = TrainSerializer
    permission_classes = []
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['cancelled', 'date']


class StopoverViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows stopovers to be viewed or edited.
    """
    queryset = Stopover.objects.all()
    serializer_class = StopoverSerializer
    permission_classes = []

class RemarkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows remarks to be viewed or edited.
    """
    queryset = Remark.objects.all()
    serializer_class = RemarkSerializer
    permission_classes = []