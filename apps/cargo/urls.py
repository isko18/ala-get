from django.urls import path
from apps.cargo.views import cargo

urlpatterns = [
    path('cargo/', cargo, name="cargo"),
]