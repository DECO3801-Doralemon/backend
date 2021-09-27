from django.contrib import admin
from .models import CommunityRecipe


class CommunityRecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipe', 'date_time_created')
    search_fields = ('id', 'recipe', 'date_time_created')


admin.site.register(CommunityRecipe, CommunityRecipeAdmin)
