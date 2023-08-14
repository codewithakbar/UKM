from django.contrib import admin

from modeltranslation.admin import TranslationAdmin
from mptt.admin import DraggableMPTTAdmin

from .models import ProductCategories, Products


@admin.register(ProductCategories)
class ProductCategoriesAdmin(DraggableMPTTAdmin, TranslationAdmin):
    list_display = ('tree_actions', 'indented_title')
    prepopulated_fields = {'slug': ('name',)}
    fields = ("image", "name", "parent", "slug")
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



@admin.register(Products)
class ProductAdmin(DraggableMPTTAdmin, TranslationAdmin):
    list_display = ('tree_actions', 'indented_title')
    fields = ("image", "name", "desc", "category")
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
