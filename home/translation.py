from modeltranslation.translator import translator, TranslationOptions
from .models import Banner, Categoy, SideCategory, Tanishuv, Jarayon, IshlabChiqrish


class BannerTranslationOptions(TranslationOptions):
    fields = ('name', 'title', 'desc')


class CategoyTranslationOptions(TranslationOptions):
    fields = ('name',)


class SideCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class TanishuvTranslationOptions(TranslationOptions):
    fields = ('title', 'desc')


class JarayonTranslationOptions(TranslationOptions):
    fields = ('title', 'desc')


class IshlabChiqrishTranslationOptions(TranslationOptions):
    fields = ('title', 'desc')


translator.register(Banner, BannerTranslationOptions)
translator.register(Categoy, CategoyTranslationOptions)
translator.register(SideCategory, SideCategoryTranslationOptions)
translator.register(Tanishuv, TanishuvTranslationOptions)
translator.register(Jarayon, JarayonTranslationOptions)
translator.register(IshlabChiqrish, IshlabChiqrishTranslationOptions)
