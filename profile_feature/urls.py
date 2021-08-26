from django.urls import path
from .views import Profile, EditPassword

urlpatterns = [
    path('', Profile.as_view(), name = 'profile'),
    path('edit-password', EditPassword.as_view(), name = 'edit-password'),
]
