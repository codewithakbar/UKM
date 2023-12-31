from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from mptt.admin import DraggableMPTTAdmin

from .models import Banner, Categoy, SideCategory, Tanishuv, Jarayon, IshlabChiqrish, Aksiyodorlar, Raxbariyat, RaxbariyatTable, Texnika, TexnikaTable



class RaxbariyatTableInline(admin.TabularInline):
    model = RaxbariyatTable
    fields = ("desc_uz", "desc_ru", "desc_en")
    extra = 1


class TexnikaTableInline(admin.TabularInline):
    model = TexnikaTable
    fields = ("title_uz", "title_ru", "title_en", "kub_uz", "kub_ru", "kub_en", "sigim_uz", "sigim_ru", "sigim_en")
    extra = 1



@admin.register(Banner)
class BannerAdmin(TranslationAdmin, DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title')
    fields = (("name_uz", "name_ru", "name_en"), ("title_uz", "title_ru", "title_en"), ("desc_uz", "desc_ru", "desc_en"),"image")
    mptt_indent_field = "name"
    group_fieldsets = True



@admin.register(Categoy)
class CategoyAdmin(DraggableMPTTAdmin, TranslationAdmin):
    list_display = ('tree_actions', 'indented_title', "status")
    prepopulated_fields = {'slug': ('name',)}
    fields = ("name", "parent", "slug", "status")
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
    inlines = [RaxbariyatTableInline]
    list_display = ('tree_actions', 'indented_title')
    fields = ("title", "lavozim", "image", "category")
    mptt_indent_field = "name"
    group_fieldsets = True




@admin.register(Texnika)
class TexnikaAdmin(DraggableMPTTAdmin, TranslationAdmin):

    inlines = [TexnikaTableInline]
    list_display = ('tree_actions', 'indented_title')
    fields = ("title", "madel", "image", "category", "desc")
    mptt_indent_field = "name"
    group_fieldsets = True




# @admin.register(Jarayon)
# class JarayonAdmin(DraggableMPTTAdmin, TranslationAdmin):
#     list_display = ('tree_actions', 'indented_title', 'formatted_created_at')
#     fields = ('image', 'title', 'desc')
#     mptt_indent_field = 'name'
#     group_fieldsets = True




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


