from django.shortcuts import render
from inventory.models import Item
from django.contrib.auth.decorators import login_required

@login_required
def item_list(request):
    items = Item.objects.filter(is_active=True).order_by('name')
    return render(request, 'inventory/item_list.html', {'items': items})
