from django.urls import path
from inventory.views.item_views import item_list
from inventory.views.transaction_views import create_inventory_transaction
from inventory.views.dashboard_views import dashboard

urlpatterns = [
    path('items/', item_list, name='item-list'),
    path('transaction/create/', create_inventory_transaction, name='create-transaction'),
    path('', dashboard, name="dashboard"),
]



