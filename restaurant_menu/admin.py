from django.contrib import admin
from .models import Item

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal", "status", "description")
    list_filter = ("status",)
    search_fields = ("description","meal")

admin.site.register(Item, MenuItemAdmin)