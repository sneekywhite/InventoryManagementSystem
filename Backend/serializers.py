# inventory/serializers.py

from rest_framework import serializers
from .models import Item, Supplier




class SupplierSerializer(serializers.ModelSerializer):
    #item_list = serializers.ListField(queryset = Item.objects.all(), many = True, source = Supplier)
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'supplier_email', 'supplier_phone']


class ItemSerializer(serializers.ModelSerializer):
    suppliers = SupplierSerializer(many=True, read_only=True)
    supplier_ids = serializers.PrimaryKeyRelatedField(
        queryset=Supplier.objects.all(), many=True, write_only=True, source='suppliers'
    )

    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price', 'suppliers', 'supplier_ids', 'quantity']

    def validate(self, data):
        """
        Check if an item with the same name already exists.
        """
        if Item.objects.filter(name=data['name']).exists():
            raise serializers.ValidationError("An item with this name already exists.")
        return data


