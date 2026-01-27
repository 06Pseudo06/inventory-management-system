from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from inventory.models import Item


@login_required
def item_list(request):
    items_qs = Item.objects.filter(is_active=True).order_by("name")

    paginator = Paginator(items_qs, 10)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "items": page_obj,        
        "page_obj": page_obj,
    }

    return render(request, "inventory/item_list.html", context)
