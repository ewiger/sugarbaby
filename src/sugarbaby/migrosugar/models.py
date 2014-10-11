from django.db import models


class ProductInfo(models.Model):

    name = models.CharField(max_length=60, unique=True)

    # Global Trade Item Number
    gtin = models.CharField(max_length=60)

    # Used to check if we have enough free space when cloning (in MB).
    disk_size = models.PositiveIntegerField()

    def __repr__(self):
        return 'Product (#%s): <%s>' % (self.gtin, self.name)

    def __str__(self):
        return self.name
