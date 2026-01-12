from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.exceptions import PermissionDenied

from inventory.models import Item, Transaction


@login_required
def dashboard(request):
    if not request.user.is_staff:
        raise PermissionDenied

    all_items = Item.objects.all()
    low_stock_qs = Item.objects.low_stock()
    recent_txn_qs = Transaction.objects.recent(6)

    # Chart data → ALL items
    stock_chart_data = list(
        all_items.values("name", "quantity")
    )

    context = {
        "total_items": all_items.count(),
        "active_items": Item.objects.active().count(),
        "low_stock_items": low_stock_qs,
        "recent_transactions": recent_txn_qs,
        "stock_chart_data": stock_chart_data,
    }

    return render(request, "inventory/dashboard.html", context)
