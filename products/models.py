from django.db import models

from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from ckeditor.fields import RichTextField




class ProductCategories(MPTTModel):
    name = models.CharField(max_length=233)
    image = models.ImageField(upload_to="prodCategories/%Y/%m/%d/")
    slug = models.SlugField()
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="children")

    def __str__(self) -> str:
        return self.name_uz




class Products(MPTTModel):
    name = models.CharField(max_length=233)
    image = models.ImageField(upload_to="products/%Y/%m/%d/")
    desc = RichTextField()
    category = TreeForeignKey(to=ProductCategories, on_delete=models.CASCADE, related_name='categories')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="children")

    def __str__(self) -> str:
        return self.name
    

