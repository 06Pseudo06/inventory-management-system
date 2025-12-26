import logging
from django.db import transaction as db_transaction
from django.core.exceptions import ValidationError, PermissionDenied
from inventory.models import Item, Transaction

logger = logging.getLogger("inventory")



@db_transaction.atomic
def create_transaction(
    *,
    item: Item,
    transaction_type: str,
    quantity: int,
    user,
    remark: str = ""
) -> Transaction:
    logger.info(
        "Transaction attempt: user=%s item_id=%s type=%s qty=%s",
        user.username,
        item.id,
        transaction_type,
        quantity,
    )

    if not user.is_staff:
        logger.warning(
            "Permission denied: user=%s attempted inventory transaction",
            user.username,
        )
        raise PermissionDenied("You do not have permission to perform inventory transactions.")

    item = Item.objects.select_for_update().get(pk=item.pk)

    if quantity <= 0:
        logger.warning(
            "Invalid quantity: user=%s item_id=%s qty=%s",
            user.username,
            item.id,
            quantity,
        )
        raise ValidationError("Quantity must be greater than zero.")

    if not item.is_active:
        logger.warning(
            "Inactive item transaction blocked: item_id=%s user=%s",
            item.id,
            user.username,
        )
        raise ValidationError("Cannot transact on an inactive item.")

    if transaction_type == Transaction.TRANSACTION_OUT:
        if item.quantity < quantity:
            logger.warning(
                "Insufficient stock: item_id=%s available=%s requested=%s user=%s",
                item.id,
                item.quantity,
                quantity,
                user.username,
            )
            raise ValidationError("Insufficient stock for OUT transaction.")
        item.quantity -= quantity

    elif transaction_type == Transaction.TRANSACTION_IN:
        item.quantity += quantity

    else:
        logger.error(
            "Invalid transaction type: type=%s user=%s",
            transaction_type,
            user.username,
        )
        raise ValidationError("Invalid transaction type.")

    item.save()

    txn = Transaction.objects.create(
        item=item,
        transaction_type=transaction_type,
        quantity=quantity,
        performed_by=user,
        remark=remark,
    )

    logger.info(
        "Transaction successful: txn_id=%s item_id=%s new_qty=%s user=%s",
        txn.id,
        item.id,
        item.quantity,
        user.username,
    )

    return txn
