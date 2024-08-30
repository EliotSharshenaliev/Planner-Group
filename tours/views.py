from rest_framework import viewsets, generics
from tours.models import Months, TourItem, Tourists
from tours.serializers import TourSerializer, TourItemUserSerializer, TouristsSerializer


class TourViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Months.objects.all()
    serializer_class = TourSerializer


class TourDetailView(generics.RetrieveAPIView):
    queryset = TourItem.objects.all()
    serializer_class = TourItemUserSerializer


class SaveUserToTourView(viewsets.ModelViewSet):
    queryset = Tourists.objects.all()
    serializer_class = TouristsSerializer
