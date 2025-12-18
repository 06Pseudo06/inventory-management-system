from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from inventory.models import Item, Transaction
from inventory.services.inventory_service import create_transaction


@login_required
def create_inventory_transaction(request):
    if not request.user.is_staff:
        raise PermissionDenied

    items = Item.objects.filter(is_active=True)

    if request.method == 'POST':
        item_id = request.POST.get('item')
        transaction_type = request.POST.get('transaction_type')
        quantity = int(request.POST.get('quantity', 0))
        remark = request.POST.get('remark', '')

        try:
            item = Item.objects.get(id=item_id)

            create_transaction(
                item=item,
                transaction_type=transaction_type,
                quantity=quantity,
                user=request.user,
                remark=remark
            )

            messages.success(request, 'Transaction created successfully.')
            return redirect('item-list')

        except Exception as e:
            messages.error(request, str(e))

    return render(
        request,
        'inventory/create_transaction.html',
        {
            'items': items,
            'transaction_types': Transaction.TRANSACTION_TYPE_CHOICES,
        }
    )
