from django.urls import path
from .views import CommunityView, MassCommunityView

urlpatterns = [
    path('recipe/<int:community_recipe_id>', CommunityView.as_view(), name="recipe"),
    path('recipe', CommunityView.as_view(), name="recipe"),
    path('', MassCommunityView.as_view(), name="feed"),
]
