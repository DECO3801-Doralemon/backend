from django.urls import path
from .views import ShoppingView
urlpatterns = [
    path('', ShoppingView.as_view(), name = 'shopping'),
]
