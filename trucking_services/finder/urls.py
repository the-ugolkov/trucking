from django.urls import path
from .views import CargoCreateView

urlpatterns = [
    path('cargo/create/', CargoCreateView.as_view(), name='cargo-create'),
]