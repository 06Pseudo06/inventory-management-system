from django.db import transaction as db_transaction
from django.core.exceptions import ValidationError

from inventory.models import Item, Transaction


@db_transaction.atomic
def create_transaction(
    *,
    item: Item,
    transaction_type: str,
    quantity: int,
    user,
    remark: str = ""
) -> Transaction:
    """
    Create an inventory transaction and update item quantity atomically.

    Guarantees:
    - Atomic DB operation (all-or-nothing)
    - Row-level locking to prevent race conditions
    - Centralized validation
    """

    # 🔒 Lock the item row to prevent concurrent updates
    item = Item.objects.select_for_update().get(pk=item.pk)

    # ---- Validation ----
    if quantity <= 0:
        raise ValidationError("Quantity must be greater than zero.")

    if transaction_type == Transaction.TRANSACTION_OUT:
        if item.quantity < quantity:
            raise ValidationError("Insufficient stock for OUT transaction.")
        item.quantity -= quantity

    elif transaction_type == Transaction.TRANSACTION_IN:
        item.quantity += quantity

    else:
        raise ValidationError("Invalid transaction type.")

    # ---- Persist changes ----
    item.save()

    txn = Transaction.objects.create(
        item=item,
        transaction_type=transaction_type,
        quantity=quantity,
        performed_by=user,
        remark=remark
    )

    return txn
