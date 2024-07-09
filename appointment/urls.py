from django.urls import include, path
from rest_framework import routers
from .import views


routers = routers.DefaultRouter()
routers.register('', views.AppointmentViewset)


urlpatterns = [
    path('', include(routers.urls)),
]
