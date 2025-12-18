from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField(default=0)
    min_threshold = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
