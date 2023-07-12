from django.db import models
from cloudinary.models import CloudinaryField
from config.constants import *


class Item(models.Model):
    class Meta(object):
        db_table = 'item'

    status = models.CharField(
        'status', blank=False, default='inactive', max_length=15, db_index=True, choices=STATUS
    )

    name = models.CharField(
        'Name', blank=False, null=False, max_length=20, db_index=True, default='Anonymous'
    )
    price = models.DecimalField(
        'price', blank=False, null=False, max_digits=14, decimal_places=2
    )

    image = CloudinaryField(
        'image', blank=True, null=False,
    )
    # recomendeditemsimage = CloudinaryField(
    #     'recomendeditem', blank=True
    # )
    created_at = models.DateTimeField(
        'Created At', blank=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Updated At', blank=True, auto_now=True
    )
    isrecomendedforyou = models.BooleanField(
        "recomendeditems", default=0, blank=False,

    )
    selectedforyou = models.BooleanField(
        "selectedforyou", default=0, blank=False,

    )

    def __str__(self):
        return self.name
