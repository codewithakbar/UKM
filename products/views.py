from rest_framework import generics, viewsets, permissions
from .models import Products, ProductCategories
from .serializer import (
ProductCategoriesSerializer, ProductsSerializer
)



class ProductCategoriesViewSet(viewsets.ModelViewSet):
    queryset = ProductCategories.objects.filter(parent=None)
    serializer_class = ProductCategoriesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProductDetailViewSet(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer


    def get_queryset(self):
        category_id = self.kwargs['category_id']
        queryset = Products.objects.filter(category__id=category_id)
        return queryset
