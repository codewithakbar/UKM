"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls.i18n import i18n_patterns

from home.views import (
    AksiyodorlarViewSet, BannerViewSet, CategoyViewSet, SideCategoryViewSet,
    TanishuvViewSet, JarayonViewSet, IshlabChiqrishViewSet, RaxbariyatViewSet, TexnikaAllViewSet, TexnikaViewSet
)

from products.views import ProductsViewSet, ProductCategoriesViewSet, ProductDetailViewSet

from news.views import AllYangiliklarViewSet, YangiliklarViewSet

from rest_framework import routers


router = routers.DefaultRouter()
router.register('banners', BannerViewSet, basename='banner')
router.register('categories', CategoyViewSet, basename='category')
router.register('sidecategories', SideCategoryViewSet, basename='sidecategory')
router.register('tanishuvs', TanishuvViewSet, basename='tanishuv')
# router.register('jarayons', JarayonViewSet, basename='jarayon')
router.register('ishlabchiqrishs', IshlabChiqrishViewSet, basename='ishlabchiqrish')
router.register('products', ProductsViewSet, basename='products')
router.register('category', ProductCategoriesViewSet, basename='categories')
router.register('texnika', TexnikaAllViewSet, basename='texnikaliar')
router.register('yangilik', AllYangiliklarViewSet, basename='newse')
router.register(r'rax/(?P<category_id>\d+)', RaxbariyatViewSet, basename='raxbarlar')
router.register(r'news/(?P<category_id>\d+)', YangiliklarViewSet, basename='news')
router.register(r'tex/(?P<category_id>\d+)', TexnikaViewSet, basename='texnika')
router.register(r'cat/(?P<category_id>\d+)', AksiyodorlarViewSet, basename='aksiyodorlar')
router.register(r'product/detail/(?P<category_id>\d+)', ProductDetailViewSet, basename='detail')

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("", include(router.urls))
]

urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }), ]


