from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from martial_arts.forms import MartialArtCreateForm, MartialArtEditForm
from martial_arts.models import MartialArt


class MartialArtListView(ListView):
    model = MartialArt


class MartialArtDetailView(DetailView):
    model = MartialArt


class MartialArtCreateView(CreateView):
    model = MartialArt
    form_class = MartialArtCreateForm
    success_url = reverse_lazy('martial-art-list')


class MartialArtUpdateView(UpdateView):
    model = MartialArt
    form_class = MartialArtEditForm
    success_url = reverse_lazy('martial-art-list')


class MartialArtDeleteView(DeleteView):
    model = MartialArt
    success_url = reverse_lazy('martial-art-list')