from django.db import models

from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey


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
    desc = models.TextField()
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="children")

    image = models.ImageField(upload_to="yangiliklar/%Y/%m", height_field=None, width_field=None, max_length=None)

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.title



#Producsiya
class IshlabChiqrish(MPTTModel):
    title = models.CharField(max_length=232)
    desc = models.TextField()
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="children")

    image = models.ImageField(upload_to="yangiliklar/%Y/%m", height_field=None, width_field=None, max_length=None)

    def __str__(self) -> str:
        return self.title
    
    

class HomePage(MPTTModel):

    name = models.CharField(max_length=232)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="children")

    def __str__(self) -> str:
        return self.name
    