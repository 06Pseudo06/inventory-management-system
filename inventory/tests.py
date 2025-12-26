from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError, PermissionDenied

from inventory.models import Item, Transaction
from inventory.services.inventory_service import create_transaction


class InventoryServiceTests(TestCase):

    def setUp(self):
        self.staff = User.objects.create_user(
            username="staff",
            password="pass",
            is_staff=True
        )

        self.user = User.objects.create_user(
            username="user",
            password="pass",
            is_staff=False
        )

        self.item = Item.objects.create(
            name="Test Item",
            quantity=10,
            min_threshold=2,
            is_active=True
        )

    def test_in_transaction_increases_quantity(self):
        create_transaction(
            item=self.item,
            transaction_type=Transaction.TRANSACTION_IN,
            quantity=5,
            user=self.staff
        )

        self.item.refresh_from_db()
        self.assertEqual(self.item.quantity, 15)
        self.assertEqual(Transaction.objects.count(), 1)

    def test_out_transaction_fails_if_insufficient_stock(self):
        with self.assertRaises(ValidationError):
            create_transaction(
                item=self.item,
                transaction_type=Transaction.TRANSACTION_OUT,
                quantity=20,
                user=self.staff
            )

        self.item.refresh_from_db()
        self.assertEqual(self.item.quantity, 10)
        self.assertEqual(Transaction.objects.count(), 0)

    def test_non_staff_user_cannot_create_transaction(self):
        with self.assertRaises(PermissionDenied):
            create_transaction(
                item=self.item,
                transaction_type=Transaction.TRANSACTION_IN,
                quantity=1,
                user=self.user
            )

        self.item.refresh_from_db()
        self.assertEqual(self.item.quantity, 10)
        self.assertEqual(Transaction.objects.count(), 0)

    def test_atomicity_rolls_back_on_failure(self):
        try:
            create_transaction(
                item=self.item,
                transaction_type=Transaction.TRANSACTION_OUT,
                quantity=999,
                user=self.staff
            )
        except ValidationError:
            pass

        self.item.refresh_from_db()
        self.assertEqual(self.item.quantity, 10)
        self.assertEqual(Transaction.objects.count(), 0)
