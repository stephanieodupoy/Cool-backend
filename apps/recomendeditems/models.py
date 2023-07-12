from django.db import models
from cloudinary.models import CloudinaryField
from config.constants import *


class RecomendedItem(models.Model):
    class Meta(object):
        db_table = 'recomendeditem'

    status = models.CharField(
        'status', blank=False, default='inactive', max_length=15, db_index=True, choices=STATUS
    )

    recomendedname = models.CharField(
        'Name', blank=False, null=False, max_length=20, db_index=True, default='Anonymous'
    )
    recomendedprice = models.DecimalField(
        'price', blank=False, null=False, max_digits=14, decimal_places=2
    )

    recomendedimage = CloudinaryField(
        'recomendedimage', blank=True, null=False
    )

    created_at = models.DateTimeField(
        'Created At', blank=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Updated At', blank=True, auto_now=True
    )

    def __str__(self):
        return self.recomendedname
