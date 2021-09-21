from django.urls import path
from .views import CommunityView, MassCommunityView, AddLikesCommunityView, RemoveLikesCommunityView

urlpatterns = [
    path('CommunityView', CommunityView.as_view(), name="CommunityView"),
    path('MassCommunityView', MassCommunityView.as_view(), name="MassCommunityView"),
    path('AddLikesCommunityView', AddLikesCommunityView.as_view(), name="AddLikesCommunityView"),
    path('RemoveLikesCommunityView', RemoveLikesCommunityView.as_view(), name="RemoveLikesCommunityView"),
]
