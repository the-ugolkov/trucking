from django.urls import path
from .views import CargoCreateView, CargoUpdateView

urlpatterns = [
    path('cargo/create/', CargoCreateView.as_view(), name='cargo-create'),
    path('cargo/<int:pk>/', CargoUpdateView.as_view(), name='cargo-update'),
    path('cargo/<int:pk>/', CargoUpdateView.as_view(), name='cargo-delete'),
]