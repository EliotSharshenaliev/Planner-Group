from django.contrib import admin
from django.urls import path, include, re_path
from frontend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tours.urls')),
    path('', views.index)
]
