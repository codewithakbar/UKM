from rest_framework import generics, viewsets, permissions
from .models import Banner, Categoy, Raxbariyat, SideCategory, Tanishuv, Jarayon, IshlabChiqrish, Aksiyodorlar
from .serializer import (
    BannerSerializer, CategoySerializer, RaxbariyatSerializer, SideCategorySerializer,
    TanishuvSerializer, JarayonSerializer, IshlabChiqrishSerializer, 
    AksiyodorlaSerializer
)


class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoyViewSet(viewsets.ModelViewSet):
    queryset = Categoy.objects.filter(parent=None)
    serializer_class = CategoySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SideCategoryViewSet(viewsets.ModelViewSet):
    queryset = SideCategory.objects.all()
    serializer_class = SideCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TanishuvViewSet(viewsets.ModelViewSet):
    queryset = Tanishuv.objects.all()
    serializer_class = TanishuvSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class JarayonViewSet(viewsets.ModelViewSet):
    queryset = Jarayon.objects.all()
    serializer_class = JarayonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    

class RaxbariyatViewSet(viewsets.ModelViewSet):
    queryset = Raxbariyat.objects.all()
    serializer_class = RaxbariyatSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class IshlabChiqrishViewSet(viewsets.ModelViewSet):
    queryset = IshlabChiqrish.objects.all()
    serializer_class = IshlabChiqrishSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class AksiyodorlarViewSet(viewsets.ModelViewSet):
    serializer_class = AksiyodorlaSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        queryset = Aksiyodorlar.objects.filter(category__id=category_id)
        return queryset
