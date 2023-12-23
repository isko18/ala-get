from django.urls import path
from apps.contact.views import contact

urlpatterns = [
    path('contact/', contact, name="contact"),
]