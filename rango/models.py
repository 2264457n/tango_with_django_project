# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def _str_(self): #For Python 2, use _unicode_ too
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def _str_(self): #For Python 2, use _unicode_ too
        return self.name
