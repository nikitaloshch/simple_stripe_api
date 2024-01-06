from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=999)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=255)
    items = models.ManyToManyField('Item')
    discount = models.ForeignKey('Discount', on_delete=models.SET_NULL, null=True, blank=True)
    tax = models.ForeignKey('Tax', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


    @property
    def total_price(self):
        total = sum(item.price for item in self.items.all())
        if self.discount:
            total -= self.discount.amount
        if self.tax:
            total += self.tax.amount
        return total


class Discount(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Tax(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

