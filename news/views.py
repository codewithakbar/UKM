from django.shortcuts import render
from rest_framework import generics, viewsets, permissions

from .models import Yangiliklar

from .serializer import YangiliklarSerializer


class YangiliklarViewSet(viewsets.ModelViewSet):
    serializer_class = YangiliklarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        queryset = Yangiliklar.objects.filter(category__id=category_id)
        return queryset


class AllYangiliklarViewSet(viewsets.ModelViewSet):
    serializer_class = YangiliklarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Yangiliklar.objects.order_by("-id").all()

    