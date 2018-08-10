from django.db import models

# Create your models here.


class Note(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255, blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)

