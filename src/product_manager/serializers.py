from rest_framework import serializers
from .models import Product, Brand, Category
 
class ProductSerializer(serializers.ModelSerializer):
    #brand = serializers.SlugRelatedField(slug_field='name', queryset=Brand.objects.all())
    #category = serializers.SlugRelatedField(slug_field='title', queryset=Category.objects.all())

    brand = serializers.StringRelatedField() # resolves the "str" representation of the brand object 
    category = serializers.StringRelatedField() 

    class Meta:
        model = Product
        fields = ('name','color','brand','category','date_added','image','size')

