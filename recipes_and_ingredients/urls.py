from django.urls import path
from .views import AllRecipeView, SingleRecipeView

urlpatterns = [
    path('all', AllRecipeView.as_view(), name='all-recipes'),
    path('<int:recipe_id>', SingleRecipeView.as_view(), name='recipe'),
    path('', SingleRecipeView.as_view(), name='recipe'),
]
