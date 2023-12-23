from django.urls import path
from apps.taxi.views import taxi

urlpatterns = [
    path('taxi/', taxi, name="taxi"),
]