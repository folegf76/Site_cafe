from django.shortcuts import render
from .models import DishCategory, Dish, WhyOur, Events

# Create your views here.
def main_page(request):
    categories = DishCategory.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True, is_special=False)
    return render(request, 'main_page.html')

