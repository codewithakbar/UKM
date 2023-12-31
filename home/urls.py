from django.urls import path, include
from rest_framework import routers
from .views import (
    AksiyodorlarViewSet, BannerAPIView, CategoyAPIView, SideCategoryAPIView,
    TanishuvAPIView, JarayonAPIView, IshlabChiqrishAPIView
)

# Create a router
router = routers.DefaultRouter()

# Register your API views with the router
router.register('banners', BannerAPIView, basename='banner')
router.register('categories', CategoyAPIView, basename='category')
router.register('sidecategories', SideCategoryAPIView, basename='sidecategory')
router.register('tanishuvs', TanishuvAPIView, basename='tanishuv')
router.register('jarayons', JarayonAPIView, basename='jarayon')
router.register('ishlabchiqrishs', IshlabChiqrishAPIView, basename='ishlabchiqrish')
router.register(r'categories/(?P<category_id>\d+)/aksiyodorlar', AksiyodorlarViewSet, basename='aksiyodorlar')


urlpatterns = [
    path('', include(router.urls)),
]



"""   ISHLAMIDI   """