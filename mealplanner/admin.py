from django.contrib import admin
from .models import MealPlan


class MealPlanAdmin(admin.ModelAdmin):
    list_display = ('customer', 'recipe', 'date')
    search_fields = ('customer', 'recipe', 'date')


admin.site.register(MealPlan, MealPlanAdmin)
