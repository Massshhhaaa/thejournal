from django.db import models
from django.db.models.signals import pre_save
from pytils.translit import slugify

# Create your models here.
class Hello(models.Model):
    title = models.CharField('Название', max_length=200)
    slug = models.SlugField('url', unique=True, null=True, blank=True)
    img = models.ImageField(upload_to='static/img', null=True, blank=True)
    excerption = models.CharField('Отрывок', max_length=255)
    annotation = models.TextField('Аннотация')


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

#
# def slug_generator(sender, instance, *args,**kwargs):
#     if not instance.slug:
#         instance.slug = 'SLUG'
#
# pre_save.connect(slug_generator, sender=Hello)
