from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
from category.utils import check_image_size


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    image = models.ImageField(upload_to='category/', validators=[
        FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'webp']), check_image_size],
                              blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class PriceList(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Consultation(models.Model):
    price_list = models.ForeignKey(PriceList, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    price = models.CharField(max_length=250)

    def __str__(self):
        return self.title
