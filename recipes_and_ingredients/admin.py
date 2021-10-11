from django.contrib import admin
from .models import *


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'kg_used')
    search_fields = ('ingredient',)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'time_created', 'name')
    search_fields = ('id', 'author', 'time_created', 'name')


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'gtin', 'name')
    search_fields = ('id', 'gtin', 'name')


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')


admin.site.register(Tag, TagAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
