from django.urls import path

from curriculum.views import (
    CurriculumItemListView,
    CurriculumItemDetailView,
    CurriculumItemCreateView,
)

urlpatterns = [
    path('', CurriculumItemListView.as_view(), name='curriculum-list'),
    path('create/', CurriculumItemCreateView.as_view(), name='curriculum-create'),
    path('<int:pk>/', CurriculumItemDetailView.as_view(), name='curriculum-detail'),
]