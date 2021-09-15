from django.contrib import admin
from .models import MealPlan


class MealPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'recipe', 'date')
    search_fields = ('id', 'customer', 'recipe', 'date')


admin.site.register(MealPlan, MealPlanAdmin)
