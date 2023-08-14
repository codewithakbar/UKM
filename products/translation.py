from modeltranslation.translator import TranslationOptions, register

from products.models import ProductCategories, Products



@register(ProductCategories)
class ProductCategoriesTranslationOptions(TranslationOptions):
    fields = ('name', 'slug')


@register(Products)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'desc')


