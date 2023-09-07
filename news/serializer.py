from rest_framework import serializers
from rest_framework.reverse import reverse
from drf_writable_nested import WritableNestedModelSerializer


from . models import Yangiliklar



class YangiliklarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Yangiliklar
        fields = ['id', 'title_uz', 'title_ru', 'title_en', 'desc_uz', 'desc_ru', 'desc_en', 'image', 'date']


    