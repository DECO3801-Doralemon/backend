from django.contrib import admin
from .models import *


class StoredIngredientAdmin(admin.ModelAdmin):
    list_display = ('customer', 'ingredient', 'expiry_date',
                    'kg_in_freezer', 'kg_in_fridge', 'kg_in_pantry')
    search_fields = ('customer', 'ingredient',)


admin.site.register(StoredIngredient, StoredIngredientAdmin)
