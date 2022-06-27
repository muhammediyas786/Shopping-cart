from django.db import models

# Create your models here.
from django.urls import reverse


class category(models.Model):
    def __str__(self):
        return self.c_name

    c_name = models.CharField(max_length=150, unique=True)
    c_slug = models.SlugField(max_length=150, unique=True)

    def get_url(self):
        return reverse('c_slug', args=[self.c_slug])


class products(models.Model):
    def __str__(self):
        return self.p_name

    p_name = models.CharField(max_length=150, unique=True)
    p_slug = models.CharField(max_length=150, unique=True)
    p_desc = models.TextField()
    p_img = models.ImageField(upload_to='products_img')
    p_price = models.IntegerField()
    p_stock = models.IntegerField()
    p_available = models.BooleanField()
    p_category = models.ForeignKey(category, on_delete=models.CASCADE)

    def get_url(self):
        return reverse('details', args=[self.p_category.c_slug, self.p_slug])
