from django.urls import path
from .views import MealPlanner

urlpatterns = [
    path('<int:year>/<int:month>/<int:day>', MealPlanner.as_view(), name = 'meal-planner'),
]
