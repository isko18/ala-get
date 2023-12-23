from django.urls import path
from apps.betaxist.views import betaxist

urlpatterns = [
    path('betaxist/', betaxist, name="betaxist"),
]