from django.db import models
from apps.users.models import User
from apps.items.models import Item
# from apps.recomendeditems.models import RecomendedItem
# from apps.recomendeditems.models import RecomendedItem


class Cart(models.Model):
    class Meta:
        db_table = 'cart'

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, db_index=True
    )
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, db_index=True
    )
    # recomendeditems = models.ForeignKey(
    #     RecomendedItem, on_delete=models.CASCADE, db_index=True
    # )
    quantity = models.IntegerField(
        'Quantity', blank=False, null=False, db_index=True
    )
    size = models.CharField(
        'Size', blank=False, null=False, max_length=20, db_index=True, default='size'
    )
    created_at = models.DateTimeField(
        'Created At', blank=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Updated At', blank=True, auto_now=True
    )
