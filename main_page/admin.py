from django.contrib import admin
from .models import DishCategory, Dish, WhyOur, Events

# Register your models here.
admin.site.register(DishCategory)
admin.site.register(Dish)
admin.site.register(WhyOur)
admin.site.register(Events)