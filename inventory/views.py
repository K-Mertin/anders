from inventory.models import Product
from inventory.serializers import ProductSerializer,ProductViewSerializer
from django.http import Http404,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
import json,datetime
from rest_framework.parsers import JSONParser,FormParser,MultiPartParser

def hello_world(request):
    return HttpResponse("Hello World!")

class ProductView(APIView):
    def get(self, request, pk, format=None):
        products = Product.objects.filter(productCode__startswith=pk)
        serialzer = ProductViewSerializer(products, many=True)
        return Response(serialzer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(createUser=self.request.user,modifyUser=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save(modifyUser=self.request.user,modifyDate=datetime.datetime.now())
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
