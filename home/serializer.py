from rest_framework import serializers
from rest_framework.reverse import reverse
from drf_writable_nested import WritableNestedModelSerializer

from .models import Banner, Categoy, RaxbariyatTable, SideCategory, Tanishuv, Jarayon, IshlabChiqrish, Aksiyodorlar, Raxbariyat, Texnika, TexnikaTable


class BannerSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField('get_links')

    class Meta:
        model = Banner
        fields = ['id', 'title', 'name_uz', 'name_ru', 'name_en', 'desc_uz', 'desc_ru', 'desc_en', 'links', 'image']

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



class AksiyodorlaSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):

    class Meta:
        model = Aksiyodorlar
        fields = ['id', 'title_uz', 'title_ru', 'title_en', 'file', 'category']
    


class CategoySerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    yordamchi = serializers.SerializerMethodField()

    class Meta:
        model = Categoy
        fields = ['id', 'slug', 'name_uz', 'name_ru', 'name_en', 'children', 'yordamchi']

    def get_children(self, obj):
        child_categories = obj.children.all()
        child_serializer = CategoySerializer(child_categories, many=True)
        return child_serializer.data

    def get_yordamchi(self, obj):
        if obj.parent:
            return obj.parent.slug  # Adjust to the appropriate field for the parent category's name
        return None

    

class SideCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SideCategory
        fields = ['id', 'name_uz', 'name_ru', 'name_en']



class TanishuvSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tanishuv
        fields = ['id', 'title_uz', 'title_ru', 'title_en', 'desc_uz', 'desc_ru', 'desc_en']




class RaxbariyatTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaxbariyatTable
        fields = ['desc_uz', 'desc_ru', 'desc_en']



class TexnikaTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TexnikaTable
        fields = ("title", "kub", "sigim")


class RaxbariyatSerializer(serializers.ModelSerializer):
    raxbariyats = RaxbariyatTableSerializer(many=True)  

    class Meta:
        model = Raxbariyat
        fields = ['id', 'title_uz', 'title_ru', 'title_en', 'lavozim_uz', 'lavozim_ru', 'lavozim_en', 'category', 'image', 'raxbariyats']



class TexnikaSerializer(serializers.ModelSerializer):
    texnikala = TexnikaTableSerializer(many=True)  

    class Meta:
        model = Texnika
        fields = ['id', 'title_uz', 'title_ru', 'title_en', 'desc_uz', 'desc_ru', 'desc_en', 'madel_uz', 'madel_ru', 'madel_en', 'category', 'image', 'texnikala']



class JarayonSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Jarayon
        fields = ['id', 'title_uz', 'title_ru', 'title_en', 'desc_uz', 'desc_ru', 'desc_en', 'created_at', 'image']


    def get_created_at(self, instance):
        return instance.created_at.strftime('%d.%m.%Y')



class IshlabChiqrishSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):

    class Meta:
        model = IshlabChiqrish
        fields = ['id', 'title_uz', 'title_ru', 'title_en', 'desc_uz', 'desc_ru', 'desc_en', 'image']

    

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

