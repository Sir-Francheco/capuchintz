from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = RichTextUploadingField(blank=True, null = True)
    date = models.DateTimeField(auto_now_add = True)
    #add author later.

    def __str__(self):
        return self.title

    def snippest(self):
        return self.body[0:200] + '.....'

class Articles(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.SlugField()
    base_image  = models.ImageField(default='default.png', blank=False)
    body = RichTextUploadingField(blank=True, null = True)
    date = models.DateTimeField(auto_now_add = True)
    #add author later.

    def __str__(self):
        return self.title

    def snippest(self):
        return self.body[0:200] + '.....'

    def shortsnip(self):
        return self.body[0:50] + '...'
