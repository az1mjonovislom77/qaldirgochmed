from django.db import models
from django.core.validators import FileExtensionValidator
from category.utils import check_image_size


class Doctor(models.Model):
    full_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    experience = models.IntegerField(null=True, blank=True)
    institution = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='doctor/', validators=[FileExtensionValidator(
        allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'webp', 'JPG', 'JPEG', 'PNG', 'SVG', 'WEBP']),
        check_image_size], blank=True, null=True)
    specialties = models.JSONField(blank=True, null=True)
    education = models.JSONField(max_length=200, null=True, blank=True)
    works = models.JSONField(null=True, blank=True)
    services = models.JSONField(null=True, blank=True)
    achievements = models.JSONField(null=True, blank=True)
    reception = models.JSONField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    full_bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.full_name


class Stickers(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    stickers = models.ImageField(upload_to='stickers/', validators=[FileExtensionValidator(
        allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'webp', 'JPG', 'JPEG', 'PNG', 'SVG', 'WEBP']),
        check_image_size], blank=True, null=True)
