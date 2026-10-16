from django.urls import path

from martial_arts.views import (
    MartialArtListView,
    MartialArtDetailView,
    MartialArtCreateView,
    MartialArtUpdateView,
    MartialArtDeleteView,
)

urlpatterns = [
    path('', MartialArtListView.as_view(), name='martial-art-list'),
    path('<int:pk>/', MartialArtDetailView.as_view(), name='martial-art-detail'),
    path('create/', MartialArtCreateView.as_view(), name='martial-art-create'),
    path('<int:pk>/edit/', MartialArtUpdateView.as_view(), name='martial-art-edit'),
    path('<int:pk>/delete/', MartialArtDeleteView.as_view(), name='martial-art-delete'),
]