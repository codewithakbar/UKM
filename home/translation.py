from modeltranslation.translator import TranslationOptions, register
from .models import Banner, Categoy, SideCategory, Tanishuv, Jarayon, IshlabChiqrish


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


