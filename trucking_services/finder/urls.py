from django.urls import path
from .views import CargoCreateView, CargoUpdateView, CargoListView

urlpatterns = [
    path('cargo/create/', CargoCreateView.as_view(), name='cargo-create'),
    path('cargo/<int:pk>/', CargoUpdateView.as_view(), name='cargo-update'),
    path('cargo/<int:pk>/', CargoUpdateView.as_view(), name='cargo-delete'),
    path('cargo/', CargoListView.as_view(), name='cargo-list'),
]