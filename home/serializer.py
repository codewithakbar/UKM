from rest_framework import serializers
from rest_framework.reverse import reverse
from drf_writable_nested import WritableNestedModelSerializer

from .models import Banner, Categoy, SideCategory, Tanishuv, Jarayon, IshlabChiqrish, HomePage


class BannerSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField('get_links')
    class Meta:
        model = Banner
        fields = ['id', 'name', 'image', 'title', 'desc', 'links']

    def get_links(self, obj):
        request = self.context['request']
        links = {
                'self': reverse('banner-detail',
                kwargs = {'pk': obj.pk}, request=request),
                # 'business': None,
                }

        # if obj.business:
        #     links['business'] = reverse('business-detail',
        #         kwargs = {'pk': obj.business}, request=request)        
        return links

class CategoySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Categoy
        fields = ['id', 'name']


class SideCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SideCategory
        fields = ['id', 'name']


class TanishuvSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tanishuv
        fields = ['id', 'title', 'desc']


class JarayonSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):

    class Meta:
        model = Jarayon
        fields = ['id', 'title', 'desc', 'image']


class IshlabChiqrishSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):

    class Meta:
        model = IshlabChiqrish
        fields = ['id', 'title', 'desc', 'image']

    

class HomePageSerializer(serializers.ModelSerializer):
    # banner = BannerSerializer(read_only = False)
    category = CategoySerializer(read_only = False)
    side_category = SideCategorySerializer(read_only = False)
    tanishuv = TanishuvSerializer(read_only = False)
    jarayon = JarayonSerializer(read_only = False)
    ishlab_chiqish = IshlabChiqrishSerializer(read_only = False)

    class Meta:
        fields = [
            'category', 'side_category', 'tanishuv', 'jarayon', 'ishlab_chiqish'
        ]
