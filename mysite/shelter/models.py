from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('category', kwargs={'category_id': self.pk})


class Pet(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=None)

    def __str__(self):
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(default=None)
    pets = models.ManyToManyField(Pet)