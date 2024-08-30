from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tours.views import TourViewSet, TourDetailView, SaveUserToTourView

router = DefaultRouter()
router.register(r'available-tours', TourViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tour-details/<int:pk>/', TourDetailView.as_view(), name='tour-detail'),
    path('save-user/', SaveUserToTourView.as_view({'post': 'create', "delete": "destroy"}), name='tour-detail'),
]
