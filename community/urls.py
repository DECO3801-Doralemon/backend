from django.urls import path
from .views import CommunityView, MassCommunityView, AddLikesCommunityView, RemoveLikesCommunityView

urlpatterns = [
    path('recipe/<int:community_recipe_id>', CommunityView.as_view(), name="recipe"),
    path('', MassCommunityView.as_view(), name="feed"),
    path('AddLikesCommunityView', AddLikesCommunityView.as_view(), name="AddLikesCommunityView"),
    path('RemoveLikesCommunityView', RemoveLikesCommunityView.as_view(), name="RemoveLikesCommunityView"),
]
