from django.contrib import admin
from .models import *


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'kg_used')
    search_fields = ('ingredient',)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'time_created', 'name')
    search_fields = ('id', 'author', 'time_created', 'name')


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('gtin', 'name')
    search_fields = ('gtin', 'name')


admin.site.register(Tag)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
