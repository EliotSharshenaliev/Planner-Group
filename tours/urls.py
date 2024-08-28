from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tours.views import TourViewSet, TourDetailView

router = DefaultRouter()
router.register(r'available-tours', TourViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tour-details/<int:pk>/', TourDetailView.as_view(), name='tour-detail'),
]
