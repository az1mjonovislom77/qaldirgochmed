from django.db import models
from django.core.validators import FileExtensionValidator

from category.utils import check_image_size


class HomepageStats(models.Model):
    experience = models.CharField(max_length=100)
    specialists = models.CharField(max_length=100)
    happy_patients = models.CharField(max_length=100)
    work_time = models.CharField(max_length=100)

    def __str__(self):
        return str(self.experience)


class FooterImage(models.Model):
    image = models.ImageField(upload_to='footer/', validators=[
        FileExtensionValidator(
            allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'webp', 'JPG', 'JPEG', 'PNG', 'SVG', 'WEBP']),
        check_image_size], blank=True, null=True)

    def __str__(self):
        return str(self.image)


class FooterPage(models.Model):
    image = models.ImageField(upload_to='footer/', validators=[
        FileExtensionValidator(
            allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'webp', 'JPG', 'JPEG', 'PNG', 'SVG', 'WEBP']),
        check_image_size], blank=True, null=True)

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, null=True, blank=True)
    works = models.JSONField(max_length=500, null=True, blank=True)


class Terapy(models.Model):
    image = models.ImageField(upload_to='footer/', validators=[
        FileExtensionValidator(
            allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'webp', 'JPG', 'JPEG', 'PNG', 'SVG', 'WEBP']),
        check_image_size], blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, null=True, blank=True)
    advantages = models.JSONField(max_length=500, null=True, blank=True)


class TypeTerapy(models.Model):
    terapy = models.ForeignKey(Terapy, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='footer/', validators=[
        FileExtensionValidator(
            allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'webp', 'JPG', 'JPEG', 'PNG', 'SVG', 'WEBP']),
        check_image_size], blank=True, null=True)
    title = models.CharField(max_length=100)
    types = models.JSONField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.title)


class SocialMedia(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='social_media/', validators=[
        FileExtensionValidator(
            allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'webp', 'JPG', 'JPEG', 'PNG', 'SVG', 'WEBP']),
        check_image_size], blank=True, null=True)
    link = models.URLField()

    def __str__(self):
        return self.name


class Location(models.Model):
    country = models.CharField(max_length=100, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    house = models.CharField(max_length=50, null=True, blank=True)
    postalCode = models.CharField(max_length=20, null=True, blank=True)
    fullAddress = models.TextField(null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.country}, {self.region}, {self.district}"


class AboutClinic(models.Model):
    number = models.JSONField(max_length=200)
    email = models.JSONField(max_length=200)
    work_time = models.CharField(max_length=100)

    def __str__(self):
        return self.email
