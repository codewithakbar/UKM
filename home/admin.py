from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from mptt.admin import DraggableMPTTAdmin

from .models import Banner, Categoy, SideCategory, Tanishuv, Jarayon, IshlabChiqrish

@admin.register(Banner)
class BannerAdmin(DraggableMPTTAdmin, TranslationAdmin):
    list_display = ('tree_actions', 'indented_title')
    fields = ("name", "image", "title", "desc")
    mptt_indent_field = "name"
    group_fieldsets = True

@admin.register(Categoy)
class CategoyAdmin(DraggableMPTTAdmin, TranslationAdmin):
    list_display = ('tree_actions', 'indented_title')
    fields = ("name",)
    mptt_indent_field = "name"
    group_fieldsets = True

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

@admin.register(Jarayon)
class JarayonAdmin(DraggableMPTTAdmin, TranslationAdmin):
    list_display = ('tree_actions', 'indented_title')
    fields = ("title", "desc")
    mptt_indent_field = "name"
    group_fieldsets = True

@admin.register(IshlabChiqrish)
class IshlabChiqrishAdmin(DraggableMPTTAdmin, TranslationAdmin):
    list_display = ('tree_actions', 'indented_title')
    fields = ("title", "desc", "image")
    mptt_indent_field = "name"
    group_fieldsets = True
