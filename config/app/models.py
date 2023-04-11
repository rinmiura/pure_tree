from django.db import models


class Menu(models.Model):

    name = models.CharField(verbose_name='name', max_length=100, blank=False, unique=True)
    parent = models.CharField(verbose_name='parent', max_length=100, blank=True)

    def __str__(self):
        return self.name
