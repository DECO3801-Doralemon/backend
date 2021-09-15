from django.contrib import admin
from .models import StoredIngredientInFreezer, StoredIngredientInFridge, StoredIngredientInPantry


class StoredIngredientInFreezerAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'ingredient', 'expiry_date', 'kg')
    search_fields = ('id', 'customer', 'ingredient')


class StoredIngredientInFridgeAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'ingredient', 'expiry_date', 'kg')
    search_fields = ('id', 'customer', 'ingredient')


class StoredIngredientInPantryAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'ingredient', 'expiry_date', 'kg')
    search_fields = ('id', 'customer', 'ingredient')


admin.site.register(StoredIngredientInFreezer, StoredIngredientInFreezerAdmin)
admin.site.register(StoredIngredientInFridge, StoredIngredientInFridgeAdmin)
admin.site.register(StoredIngredientInPantry, StoredIngredientInPantryAdmin)
