from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Item, Category

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'user', 'is_approved')
    list_filter = ('status', 'is_approved')
    actions = ['approve_items']

    def approve_items(self, request, queryset):
        queryset.update(is_approved=True)
        self.message_user(request, "Selected items have been approved.")
    approve_items.short_description = "Approve selected items"

admin.site.register(Category)
