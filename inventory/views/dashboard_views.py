from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.exceptions import PermissionDenied

from inventory.models import Item, Transaction


@login_required
def dashboard(request):
    if not request.user.is_staff:
        raise PermissionDenied

    low_stock_qs = Item.objects.low_stock()
    recent_txn_qs = Transaction.objects.recent(20)

    # ✅ Convert queryset → serializable data
    stock_chart_data = list(
        low_stock_qs.values("name", "quantity")
    )

    context = {
        "total_items": Item.objects.count(),
        "active_items": Item.objects.active().count(),
        "low_stock_items": low_stock_qs,
        "recent_transactions": recent_txn_qs,
        "stock_chart_data": stock_chart_data,
    }

    return render(request, "inventory/dashboard.html", context)
