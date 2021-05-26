
from django.urls import path
from .views import BookmarkListView
from .views import BookmarkDetailView
from .views import BookmarkCreateView, BookmarkUpdateView, BookmarkDeleteView
from .views import info

app_name = "bookmark"

urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),
    path('info/', info, name='info'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),
]
