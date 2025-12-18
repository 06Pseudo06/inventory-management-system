from django.contrib import admin, messages
from .models import Item, Transaction
from inventory.services.inventory_service import create_transaction


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'min_threshold', 'is_active')
    search_fields = ('name',)
    list_filter = ('is_active',)
    readonly_fields = ('quantity', 'created_at', 'updated_at')

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser



@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_type', 'item', 'quantity', 'performed_by', 'created_at')
    list_filter = ('transaction_type', 'created_at')
    readonly_fields = ('created_at',)

    def has_add_permission(self, request):
        return request.user.is_staff

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

