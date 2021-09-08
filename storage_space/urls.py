from django.urls import path
from .views import FreezerStorageView, FridgeStorageView, PantryStorageView

urlpatterns = [
    path('freezer', FreezerStorageView.as_view(), name = 'storage-freezer'),
    path('fridge', FridgeStorageView.as_view(), name = 'storage-fridge'),
    path('pantry', PantryStorageView.as_view(), name = 'storage-pantry'),
]
