from django.urls import path
from apps.base.views import settings, politikConfidital, soglashenie, LicenseAgreement

urlpatterns = [
    path('', settings, name="index"),
    path('politikConfidital/', politikConfidital, name="politikConfidital"),
    path('soglashenie/', soglashenie, name="soglashenie"),
    path('LicenseAgreement/', LicenseAgreement, name="LicenseAgreement"),
]