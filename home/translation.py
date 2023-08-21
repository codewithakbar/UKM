from modeltranslation.translator import TranslationOptions, register

from products.models import ProductCategories
from .models import Banner, Categoy, RaxbariyatTable, SideCategory, Tanishuv, Jarayon, IshlabChiqrish, Aksiyodorlar, Raxbariyat


@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('name', 'title', 'desc')


@register(Categoy)
class CategoyTranslationOptions(TranslationOptions):
    fields = ('name','slug')


@register(SideCategory)
class SideCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Tanishuv)
class TanishuvTranslationOptions(TranslationOptions):
    fields = ('title', 'desc')


@register(Jarayon)
class JarayonTranslationOptions(TranslationOptions):
    fields = ('title', 'desc')


@register(IshlabChiqrish)
class IshlabChiqrishTranslationOptions(TranslationOptions):
    fields = ('title', 'desc')


@register(Aksiyodorlar)
class AksiyodorlarTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(Raxbariyat)
class RaxbariyatTranslationOptions(TranslationOptions):
    fields = ('title', 'lavozim')


@register(RaxbariyatTable)
class RaxbariyatTableTranslationOptions(TranslationOptions):
    fields = ('desc', )