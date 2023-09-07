from django.db import models

from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from ckeditor.fields import RichTextField




class Yangiliklar(MPTTModel):

    title = models.CharField(max_length=233)
    desc = RichTextField()
    image = models.ImageField(upload_to='news/%Y/%m/%d')
    date = models.DateTimeField(auto_now_add=True)


    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="yangilik")

    def __str__(self) -> str:
        return self.title
    



