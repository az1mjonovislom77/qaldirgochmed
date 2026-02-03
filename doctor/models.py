from django.db import models
from django.core.validators import FileExtensionValidator
from category.utils import check_image_size


class Doctor(models.Model):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='doctor/', validators=[FileExtensionValidator(
        allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'webp', 'JPG', 'JPEG', 'PNG', 'SVG', 'WEBP']),
        check_image_size], blank=True, null=True)
    profession = models.CharField(max_length=100)
    experience = models.IntegerField()
    education = models.CharField(max_length=200)
    works = models.JSONField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.full_name


class Stickers(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    stickers = models.ImageField(upload_to='stickers/', validators=[FileExtensionValidator(
        allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'webp', 'JPG', 'JPEG', 'PNG', 'SVG', 'WEBP']),
        check_image_size], blank=True, null=True)