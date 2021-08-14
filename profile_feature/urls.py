from django.urls import path
from .views import changeBioForm

urlpatterns = [
    path('', profile, name ='profile'),
    path('changeBioForm', changeBioForm, name = 'changeBioForm'),
    path('replaceBio', replaceBio, name='replaceBio'),
]
