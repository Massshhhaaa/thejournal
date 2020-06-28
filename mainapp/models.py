from django.db import models

# Create your models here.
class Hello(models.Model):
    title = models.CharField('Название', max_length=200)
    img = models.ImageField(upload_to='static/img', null=True, blank=True)
    excerption = models.CharField('Отрывок', max_length=255)
    annotation = models.TextField('Аннотация')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
         return reverse('model-detail-view', args=[str(self.id)])
