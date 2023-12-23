from django.urls import path
from apps.delivery.views import delivery

urlpatterns = [
    path('delivery/', delivery, name="delivery"),
]