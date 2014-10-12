from django.db import models
import datetime


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

    def get_fields(self):
        result = {}
        keys = [
            'name', 'gtin', 'image_url', 'energy', 'proteins', 'carbohydrates',
            'fats', 'base_unit', 'base_quantity',
        ]
        for key in keys:
            result[key] = getattr(self, key)
        return result


class DiaryRecord(models.Model):

    # Timestamp
    consumed = models.DateTimeField(auto_now_add=True)

    product = models.ForeignKey(ProductInfo, related_name='diary_entries')

    @staticmethod
    def get_daily_values(selected_date):
        '''selected_date is '''
        if isinstance(selected_date, basestring):
            fmt = '%Y%m%d'
            selected_date = datetime.datetime.strptime(selected_date, fmt)
        values = []
        for record in DiaryRecord.objects.filter(
            consumed__year=selected_date.year,
            consumed__month=selected_date.month,
            consumed__day=selected_date.day,
        ):
            fields = record.product.get_fields()
            fields['consumed'] = record.consumed.strftime(
                '%Y-%m-%d %H:%M')
            values.append(fields)
        return values

    def __repr__(self):
        return 'Record w/ <%s>' % (self.product.name)

    def __str__(self):
        return 'Dairy Record w/ <%s> on %s' % \
            (self.product.name,
             self.consumed.strftime('%Y-%m-%d %H:%M'))
