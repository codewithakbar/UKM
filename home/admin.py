from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from mptt.admin import DraggableMPTTAdmin

from .models import Banner, Categoy, SideCategory, Tanishuv, Jarayon, IshlabChiqrish, Aksiyodorlar, Raxbariyat

@admin.register(Banner)
class BannerAdmin(TranslationAdmin, DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title')
    fields = (("name_uz", "name_ru", "name_en"), ("title_uz", "title_ru", "title_en"), ("desc_uz", "desc_ru", "desc_en"),"image")
    mptt_indent_field = "name"
    group_fieldsets = True


@admin.register(Categoy)
class CategoyAdmin(DraggableMPTTAdmin, TranslationAdmin):
    list_display = ('tree_actions', 'indented_title')
    prepopulated_fields = {'slug': ('name',)}
    fields = ("name", "parent", "slug")
    mptt_indent_field = "name"
    group_fieldsets = True

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



@admin.register(SideCategory)
class SideCategoryAdmin(DraggableMPTTAdmin, TranslationAdmin):
    list_display = ('tree_actions', 'indented_title')
    fields = ("name",)
    mptt_indent_field = "name"
    group_fieldsets = True


@admin.register(Tanishuv)
class TanishuvAdmin(DraggableMPTTAdmin, TranslationAdmin):
    list_display = ('tree_actions', 'indented_title')
    fields = ("title", "desc")
    mptt_indent_field = "name"
    group_fieldsets = True



@admin.register(Raxbariyat)
class RaxbariyatAdmin(DraggableMPTTAdmin, TranslationAdmin):
    list_display = ('tree_actions', 'indented_title')
    fields = ("title", "desc", "image", "category")
    mptt_indent_field = "name"
    group_fieldsets = True



@admin.register(Jarayon)
class JarayonAdmin(DraggableMPTTAdmin, TranslationAdmin):
    list_display = ('tree_actions', 'indented_title', 'formatted_created_at')
    fields = ('image', 'title', 'desc')
    mptt_indent_field = 'name'
    group_fieldsets = True



@admin.register(Aksiyodorlar)
class AksiyodorlarAdmin(DraggableMPTTAdmin, TranslationAdmin):
    list_display = ('tree_actions', 'indented_title')
    fields = ('file', 'title', 'category')
    mptt_indent_field = 'name'
    group_fieldsets = True





@admin.register(IshlabChiqrish)
class IshlabChiqrishAdmin(DraggableMPTTAdmin, TranslationAdmin):
    list_display = ('tree_actions', 'indented_title')
    fields = ("title", "desc", "image")
    mptt_indent_field = "name"
    group_fieldsets = True
