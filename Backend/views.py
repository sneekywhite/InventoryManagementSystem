
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action
from .models import Item, Supplier
from .serializers import ItemSerializer, SupplierSerializer
from rest_framework.decorators import api_view
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
import logging



logger = logging.getLogger('django')

classname = 'ItemViewSet'

class ItemViewSet(viewsets.ViewSet):

    @swagger_auto_schema(
        operation_description="Retrieve a list of all items",
        responses={200: ItemSerializer(many=True)}
    )
    def list(self, request):
        items = Item.objects.all()
        if len(items) == 0:
            logger.error('No items found in database')
        
        serializer = ItemSerializer(items, many=True)

        logger.info(f"data ===> : {serializer.data}")
        return Response(serializer.data)
    

    @swagger_auto_schema(
        operation_description="Retrieve a specific item by ID",
        responses={200: ItemSerializer(), 404: 'Item not found'}
    )
    def retrieve(self, request, pk=None):
        try:
            logger.info(f"cehecking database for {request.method} =============>")
            item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ItemSerializer(item)
        return Response(serializer.data)


    # @swagger_auto_schema(
    #     request_body=openapi.Schema(
    #         type=openapi.TYPE_OBJECT,
    #         properties={
    #             'name': openapi.Schema(type=openapi.TYPE_STRING, description='Field 1 description'),
    #             'description': openapi.Schema(type=openapi.TYPE_STRING, description='Field 2 description'),
    #             'price': openapi.Schema(type=openapi.TYPE_NUMBER, description='Field 2 description'),
    #             'suppliers': openapi.Schema(type=openapi.TYPE_ARRAY, description='Field 2 description'),
    #         },
    #         required=['name', 'description', 'price', 'suppliers'],
    #         example={
    #             'name': 'default value for field1',
    #             'description': "default value for field",
    #             'price' : 123,
    #             'suppliers' :"default value for field"
    #         }
    #     )
    # )

    @swagger_auto_schema(
        operation_description="Create a new item",
        request_body=ItemSerializer,
        responses={201: ItemSerializer(), 400: 'Bad Request'}
    )
    def create(self, request: Request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
   
    @swagger_auto_schema(
        operation_description="Update an existing item by ID",
        request_body=ItemSerializer,
        responses={200: ItemSerializer(), 404: 'Item not found', 400: 'Bad Request'}
    )
    def update(self, request, pk=None):
        try:
            item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    @swagger_auto_schema(
        operation_description="Delete an existing item by ID",
        responses={204: 'No Content', 404: 'Item not found'}
    )
    def destroy(self, request, pk=None):
        methodname = request.method
        try:
            item = Item.objects.get(pk=pk)      
        except Item.DoesNotExist:
            logger.error(f"item of id {pk} not found  -------------------------------- class name: {classname} method: {methodname}")
            response ={
                "message": "item is not found",
                "data": None
            }
            return Response(data =response, status=status.HTTP_404_NOT_FOUND)
        
        item.delete()

        logger.info(f"Item deleted for id {pk}")

        return Response( status=status.HTTP_204_NO_CONTENT)



class SupplierViewSet(viewsets.ViewSet):

    @swagger_auto_schema(
        operation_description="Retrieve a list of all suppliers",
        responses={200: SupplierSerializer(many=True)}
    )
    # def list(self, request, pk=None):
    #     item = self.get_object()
    #     suppliers = item.suppliers.all()
    #     serializer = SupplierSerializer(suppliers, many=True)
    #     return Response(serializer.data)
    def list(self, request):
        suppliers = Supplier.objects.all()
        serializer = SupplierSerializer(suppliers, many=True)
        print(serializer)
        return Response(serializer.data)
        

    @swagger_auto_schema(
        operation_description="Retrieve a specific supplier by ID",
        responses={200: SupplierSerializer(), 404: 'Supplier not found'}
    )

    def retrieve(self,request,  pk=None):
        try:
    
            supplier = Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            response = {
                "message": "Supplier does not exist"
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        serializer = SupplierSerializer(supplier)
        print(serializer.data)
        return Response(serializer.data)
    
    
    @swagger_auto_schema(
        operation_description="Create a new supplier",
        request_body=SupplierSerializer,
        responses={201: SupplierSerializer(), 400: 'Bad Request'}
    )
    def create(self, request):
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    @swagger_auto_schema(
        operation_description="Update an existing supplier by ID",
        request_body=SupplierSerializer,
        responses={200: SupplierSerializer(), 404: 'Supplier not found', 400: 'Bad Request'}
    )
    def update(self, request, pk=None):
        try:
            supplier = Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SupplierSerializer(supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    @swagger_auto_schema(
        operation_description="Delete an existing supplier by ID",
        responses={204: 'No Content', 404: 'Supplier not found'}
    )
    def destroy(self, request, pk=None):
        try:
            supplier = Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        supplier.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


    







