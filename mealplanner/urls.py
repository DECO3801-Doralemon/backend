from django.urls import path
from .views import MealPlanner

urlpatterns = [
    path('', MealPlanner.as_view(), name = 'meal-planner'),
    path('<int:year>/<int:month>/<int:day>', MealPlanner.as_view(), name = 'meal-planner'),
]
