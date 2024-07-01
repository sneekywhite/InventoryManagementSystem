from django.db import models


class Supplier(models.Model):
    #supplier_id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    supplier_email = models.EmailField(max_length=255, blank=True)
    supplier_phone = models.CharField(max_length=255, blank=True)
    
    #supplied_item = models

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(null=True)
    date_added = models.DateField(auto_now_add=True)
    suppliers = models.ManyToManyField(Supplier, related_name='items')
    #supplierId = models.ForeignKey(Supplier, related_name='suppliers')

    def __str__(self):
        return self.name





