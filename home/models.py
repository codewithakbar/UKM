from django.db import models

from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from ckeditor.fields import RichTextField



class Banner(MPTTModel):
    name = models.CharField(max_length=232)
    image = models.ImageField(upload_to="banners/%Y/%m")
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="children")

    title = models.CharField(max_length=232, null=True, blank=True)
    desc = models.TextField()

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Bannerlar"

    # def __str__(self) -> str:
    #     return self.name_ru
    


class Categoy(MPTTModel):
    name = models.CharField(max_length=232)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="children")

    slug = models.SlugField(unique=True, blank=True, null=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = "Asosiy Kategoriya"
        verbose_name_plural = "Asosiy Kategoriyalar"

    def __str__(self) -> str:
        return self.name



class SideCategory(MPTTModel):
    name = models.CharField(max_length=232)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="children")

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self) -> str:
        return self.name



class Aksiyodorlar(MPTTModel):
    title = models.CharField(max_length=232)
    file = models.FileField(upload_to="media/pdf/%Y/%m/%d")
    category = models.ForeignKey(Categoy, on_delete=models.CASCADE)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="children")


    def __str__(self) -> str:
        return self.title
    


class Raxbariyat(MPTTModel):
    title = models.CharField(max_length=232)
    lavozim = models.CharField(max_length=232)
    image = models.ImageField(upload_to="raxbarlar/%Y/%m")
    category = models.ForeignKey(Categoy, on_delete=models.CASCADE)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="children")

    def __str__(self) -> str:
        return self.title



class Texnika(MPTTModel):
    title = models.CharField(max_length=232)
    madel = models.CharField(max_length=232)
    desc = RichTextField()
    image = models.ImageField(upload_to="raxbarlar/%Y/%m")
    category = models.ForeignKey(Categoy, on_delete=models.CASCADE)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="children")

    def __str__(self) -> str:
        return self.title



class Tanishuv(MPTTModel):
    title = models.CharField(max_length=232)
    desc = models.TextField()
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="children")

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self) -> str:
        return self.title



# Yangiliklar
class Jarayon(MPTTModel):
    title = models.CharField(max_length=232)
    desc = RichTextField(null=True, blank=True)

    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="children")

    image = models.ImageField(upload_to="yangiliklar/%Y/%m", height_field=None, width_field=None, max_length=None)

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.title


    @property
    def formatted_created_at(self):
        return self.created_at.strftime('%d.%m.%Y')


    class Meta:
        verbose_name = "Jarayon(Yangilik)"
        verbose_name_plural = "Jarayonlar(Yangiliklar)"



#Producsiya
class IshlabChiqrish(MPTTModel):
    title = models.CharField(max_length=232)
    desc = models.TextField()
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="children")

    image = models.ImageField(upload_to="yangiliklar/%Y/%m", height_field=None, width_field=None, max_length=None)

    def __str__(self) -> str:
        return self.title
    
    

# Tabular Inline 

class RaxbariyatTable(models.Model):

    raxbariyat = models.ForeignKey(Raxbariyat, default=None, related_name='raxbariyats', on_delete=models.CASCADE, blank=True, null=True)
    desc = RichTextField()
    

    def __str__(self) -> str:
        return self.desc


class TexnikaTable(models.Model):

    texnika = models.ForeignKey(Texnika, default=None, related_name='texnikala', on_delete=models.CASCADE, blank=True, null=True)

    title = models.CharField(max_length=233)
    kub = models.CharField(max_length=233)
    sigim = models.CharField(max_length=233)


class HomePage(MPTTModel):

    name = models.CharField(max_length=232)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="children")

    def __str__(self) -> str:
        return self.name
    