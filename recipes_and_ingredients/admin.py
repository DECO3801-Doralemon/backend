from django.contrib import admin
from .models import *


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'name')
    search_fields = ('id', 'author', 'name')


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('ingredientGTIN', 'ingredientName', 'ingredientType')
    search_fields = ('ingredientGTIN', 'ingredientName', 'ingredientType')


admin.site.register(Tag)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
