from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']


class Pet(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=None)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Pet"
        verbose_name_plural = "Pets"
        ordering = ['name']


class User(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(default=None)
    pets = models.ManyToManyField(Pet)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ['last_name']