from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

# Create your views here.
@api_view(['GET'])
def get_all_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serialized = ProductSerializer(products, many=True)
        return Response(serialized.data)