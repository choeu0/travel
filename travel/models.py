from django.db import models

from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    meta_description = models.TextField(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('travel:city_in_category', args=[self.slug])


class City(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='cities')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)

    image = models.ImageField(upload_to='cities/%Y/%m/%d',blank=True)
    description = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)

    available_display = models.BooleanField('Display', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-name']
        index_together = [['id','slug']]
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('travel:city_detail', args=[self.id, self.slug])