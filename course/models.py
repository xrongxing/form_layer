# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

# Create your models here.
TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)
class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3, choices= TITLE_CHOICES)
    brith_date = models.DateField(blank=True, null=True)
    
    def __str___(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    
    def __str__(self):
        return self.name

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title', 'brith_date']

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
