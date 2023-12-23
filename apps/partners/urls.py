from django.urls import path
from apps.partners.views import partners

urlpatterns = [
    path('partners/', partners, name="partners"),
]