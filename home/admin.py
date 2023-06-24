from django.contrib import admin

from .models import Banner, Categoy, SideCategory, Tanishuv, Jarayon, IshlabChiqrish, HomePage

from mptt.admin import DraggableMPTTAdmin


@admin.register(HomePage)
class HomePageAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title')
    fields = ("name",)
    mptt_indent_field = "name"
    group_fieldsets = True


@admin.register(Banner)
class BannerAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title')
    fields = ("name", "image", "title", "desc")
    mptt_indent_field = "name"
    group_fieldsets = True


@admin.register(Categoy)
class CategoyAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title')
    fields = ("name",)
    mptt_indent_field = "name"
    group_fieldsets = True


@admin.register(SideCategory)
class SideCategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title')
    fields = ("name", )
    mptt_indent_field = "name"
    group_fieldsets = True


@admin.register(Tanishuv)
class TanishuvAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title')
    fields = ("title", "desc")
    mptt_indent_field = "name"
    group_fieldsets = True


@admin.register(Jarayon)
class JarayonAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title')
    fields = ("title", "desc")
    mptt_indent_field = "name"
    group_fieldsets = True


@admin.register(IshlabChiqrish)
class IshlabChiqrishonAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title')
    fields = ("title", "desc", "image")
    mptt_indent_field = "name"
    group_fieldsets = True



# admin.site.register(Banner, BannerAdmin)
# admin.site.register(
#     Banner,
#     DraggableMPTTAdmin,
#     list_display=(
#     'tree_actions',
#     'indented_title',
#     ),
#     list_display_links=(
#     'indented_title',
#     ),
# )
