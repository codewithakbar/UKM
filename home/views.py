from rest_framework import generics, viewsets, permissions
from .models import Banner, Categoy, SideCategory, Tanishuv, Jarayon, IshlabChiqrish
from .serializer import (
    BannerSerializer, CategoySerializer, SideCategorySerializer,
    TanishuvSerializer, JarayonSerializer, IshlabChiqrishSerializer
)


class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoyViewSet(viewsets.ModelViewSet):
    queryset = Categoy.objects.all()
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


class IshlabChiqrishViewSet(viewsets.ModelViewSet):
    queryset = IshlabChiqrish.objects.all()
    serializer_class = IshlabChiqrishSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
