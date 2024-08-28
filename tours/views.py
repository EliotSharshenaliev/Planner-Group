from rest_framework import viewsets, generics
from tours.models import Months, TourItem
from tours.serializers import TourSerializer, TourItemUserSerializer


class TourViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Months.objects.all()
    serializer_class = TourSerializer


class TourDetailView(generics.RetrieveAPIView):
    queryset = TourItem.objects.all()
    serializer_class = TourItemUserSerializer

