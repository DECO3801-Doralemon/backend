from django.contrib import admin
from .models import *


class StoredIngredientAdmin(admin.ModelAdmin):
    list_display = ('customer', 'ingredient', 'expiry_date', 'freezer_weight', 'fridge_weight', 'pantry_weight')
    search_fields = ('customer', 'ingredient',)


admin.site.register(StoredIngredient, StoredIngredientAdmin)
