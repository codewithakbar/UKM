from rest_framework import serializers
from rest_framework.reverse import reverse
from drf_writable_nested import WritableNestedModelSerializer

from .models import Products, ProductCategories



class ProductCategoriesSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    yordamchi = serializers.SerializerMethodField()

    class Meta:
        model = ProductCategories
        fields = ['id', 'slug', 'name_uz', 'name_ru', 'name_en', 'children', 'yordamchi']

    def get_children(self, obj):
        child_categories = obj.children.all()
        child_serializer = ProductCategoriesSerializer(child_categories, many=True)
        return child_serializer.data

    def get_yordamchi(self, obj):
        if obj.parent:
            return obj.parent.slug
        return None



class ProductsSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ['id', 'name_uz', 'name_ru', 'name_en', 'desc_uz', 'desc_ru', 'desc_en', 'image', 'category']



