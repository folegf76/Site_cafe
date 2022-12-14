from django.contrib import admin
from .models import DishCategory, Dish

# Register your models here.
admin.site.register(DishCategory)
admin.site.register(Dish)