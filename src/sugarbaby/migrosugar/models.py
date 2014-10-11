from django.db import models


class ProductInfo(models.Model):

    name = models.CharField(max_length=60, unique=True)

    # Global Trade Item Number
    gtin = models.CharField(max_length=60)

    image_url = models.CharField(max_length=128)

    # disk_size = models.PositiveIntegerField()

    # Nutrient facts
    # kcal
    energy = models.FloatField()

    # g
    proteins = models.FloatField()

    # g
    carbohydrates = models.FloatField()

    # g
    fats = models.FloatField()

    base_quantity = models.FloatField()

    base_unit = models.CharField(max_length=6)

    def __repr__(self):
        return 'Product (#%s): <%s>' % (self.gtin, self.name)

    def __str__(self):
        return self.name


class DiaryRecord(models.Model):

    # Timestamp
    consumed = models.DateTimeField(auto_now_add=True)

    product = models.ForeignKey(ProductInfo, related_name='diary_entries')
