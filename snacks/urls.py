  
from django.urls import path
from django.urls.resolvers import URLPattern
from .views import SnackListView, SnackDetailView

URLPattern = [
    path('', SnackDetailView.as_view(), name='snack_list'),
    path('<int:pk>/' , SnackDetailView.as_view(), name = 'snack_detail')
]