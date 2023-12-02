from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

class Card(models.Model):
    title = models.CharField('Описание', max_length=50)
    photo = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.photo.delete()
        super().delete(*args, **kwargs)
