from django.db import models
from django.conf import settings
from .item import Item


class Transaction(models.Model):
    TRANSACTION_IN = 'IN'
    TRANSACTION_OUT = 'OUT'

    TRANSACTION_TYPE_CHOICES = [
        (TRANSACTION_IN, 'In'),
        (TRANSACTION_OUT, 'Out'),
    ]

    item = models.ForeignKey(
        Item,
        on_delete=models.PROTECT,
        related_name='transactions'
    )
    transaction_type = models.CharField(
        max_length=3,
        choices=TRANSACTION_TYPE_CHOICES
    )
    quantity = models.PositiveIntegerField()
    performed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )
    remark = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.item.name} ({self.quantity})"
