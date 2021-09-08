from django.urls import path
from .views import StorageView

urlpatterns = [
    path('', StorageView.as_view(), name = 'storage'),
]
