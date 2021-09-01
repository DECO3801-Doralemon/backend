from django.contrib import admin
from .models import *


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
    search_fields = ('user',)


# Register your models here.
admin.site.register(Customer, CustomerAdmin)
admin.site.register(WasteStat)
