from django.shortcuts import render
from rest_framework import authentication, permissions, viewsets, filters

from home.models import Banner, HomePage
from .serializer import HomePageSerializer


class HomePageViewSet(viewsets.ModelViewSet):
    queryset = HomePage.objects.order_by('name',)
    serializer_class = HomePageSerializer
