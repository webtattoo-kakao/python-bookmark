from encodings.punycode import selective_find

from django.shortcuts import render


#from django.views.generic import list
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bookmark

# Create your views here.

class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 10


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = [
        'site_name',
        'url'
    ]
    template_name_suffix = '_create'
    success_url = reverse_lazy('bookmark:list')


class BookmarkDetailView(DetailView):
    model = Bookmark


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = [
        'site_name',
        'url'
    ]
    template_name_suffix = '_update'


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:list')



