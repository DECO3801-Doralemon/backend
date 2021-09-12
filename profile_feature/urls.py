from django.urls import path
from .views import ProfileView, EditPasswordView

urlpatterns = [
    path('', ProfileView.as_view(), name = 'profile'),
    path('edit-password', EditPasswordView.as_view(), name = 'edit-password'),
]
