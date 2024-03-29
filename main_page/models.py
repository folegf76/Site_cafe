from django.db import models
from django.core.validators import RegexValidator
import uuid
import os

# Create your models here.


class DishCategory(models.Model):

    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}: {self.position}'

    class Meta:
        ordering = ('position', )


class Dish(models.Model):

    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/dishes', filename)

    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE)
    is_special = models.BooleanField(default=False)
    desc = models.TextField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    ingredients = models.CharField(max_length=100)
    photo = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.name}: {self.position}'

    class Meta:
        ordering = ('position', )


class WhyOur(models.Model):

    name = models.CharField(max_length=100, unique=True)
    position = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)
    is_about = models.BooleanField(default=False)
    desc = models.TextField(max_length=500)
    video = models.URLField(blank=True)

    def __str__(self):
        return f'{self.name}: {self.position}'

    class Meta:
        ordering = ('position', )


class Events(models.Model):

    def get_file(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/events', filename)

    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)
    desc = models.TextField(max_length=500)
    paragraph_1 = models.TextField(max_length=100, default="")
    paragraph_2 = models.TextField(max_length=100, default="")
    paragraph_3 = models.TextField(max_length=100, default="")
    desc_final = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.ImageField(upload_to=get_file)
    date = models.DateTimeField(unique=True)

    def __str__(self):
        return f'{self.name}: {self.date}'

    class Meta:
        ordering = ('position', )


class About(models.Model):

    name = models.CharField(max_length=50, unique=True)
    name_bold = models.CharField(max_length=50, blank=True)
    position = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)
    desc_1 = models.TextField(max_length=200)
    desc_2 = models.TextField(max_length=200)
    paragraph_1 = models.TextField(max_length=100)
    paragraph_2 = models.TextField(max_length=100)
    paragraph_3 = models.TextField(max_length=100)
    desc_final = models.TextField(max_length=200)
    video = models.URLField()

    def __str__(self):
        return f'{self.name}: {self.name_bold}'

    class Meta:
        ordering = ('position', )


class Gallery(models.Model):

    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/gallery', filename)

    is_visible = models.BooleanField(default=True)
    desc = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to=get_file_name)


class UserReservation(models.Model):

    phone_validator = RegexValidator(regex=r'^\+?3?8?0\d{2}[- ]?(\d[- ]?){7}$', message='не вірний номер')
    email_validator = RegexValidator(regex=r'^[0-9A-Za-z](-?[0-9A-Za-z_])+@[0-9A-Za-z](-?[0-9A-Za-z._])+$', message='не вірний email')
    time_validator = RegexValidator(regex=r'^\d{2}.\d{2}', message='введіть час в форматі хх:хх')
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, validators=[phone_validator])
    email_us = models.CharField(max_length=20, validators=[email_validator])
    persons = models.PositiveSmallIntegerField()
    message = models.TextField(max_length=250, blank=True)
    date = models.CharField(max_length=50)
    times = models.CharField(max_length=15, validators=[time_validator], blank=True)
    manager_data_processed = models.DateField(auto_now=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date', )

    def __str__(self):
        return f'{self.name} {self.phone}: {self.message[:20]}'
