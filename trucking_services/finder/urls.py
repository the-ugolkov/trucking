from django.urls import path
from .views import CargoCreateView, CargoUpdateView, CargoListView, CargoDetailView, CarUpdateView

urlpatterns = [
    path('cargo/create/', CargoCreateView.as_view(), name='cargo-create'),
    path('cargo/<int:pk>/update/', CargoUpdateView.as_view(), name='cargo-update'),
    path('cargo/<int:pk>/delete/', CargoUpdateView.as_view(), name='cargo-delete'),
    path('cargo/<int:pk>/', CargoDetailView.as_view(), name='cargo-detail'),
    path('cargo/', CargoListView.as_view(), name='cargo-list'),
    path('car/<int:pk>/', CarUpdateView.as_view(), name='car-update')
]