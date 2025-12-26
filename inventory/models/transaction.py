from django.db import models
from django.conf import settings
from .item import Item

#manager 
class TransactionQuerySet(models.QuerySet):
    def recent(self, limit=20):
        return self.order_by("-created_at")[:limit]

    def for_item(self, item):
        return self.filter(item=item)


class TransactionManager(models.Manager):
    def get_queryset(self):
        return TransactionQuerySet(self.model, using=self._db)

    def recent(self, limit=20):
        return self.get_queryset().recent(limit)

    def for_item(self, item):
        return self.get_queryset().for_item(item)


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

    objects = TransactionManager()


    def __str__(self):
        return f"{self.transaction_type} - {self.item.name} ({self.quantity})"
