from django.shortcuts import render
from .models import DishCategory, Dish, WhyOur, Events, About, Gallery
import random

# Create your views here.
def main_page(request):
    categories = DishCategory.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True, is_special=False)
    specials_dishes = Dish.objects.filter(is_visible=True, is_special=True)
    about = About.objects.filter(is_visible=True)
    why_us = WhyOur.objects.filter(is_visible=True, is_about=False)
    events = Events.objects.filter(is_visible=True)
    gallery_photos = list(Gallery.objects.filter(is_visible=True))
    gallery_photos = random.sample(gallery_photos, 8)


    return render(request, 'main_page.html', context={
        'categories': categories,
        'dishes': dishes,
        'special': specials_dishes,
        'abouts': about,
        'whyus': why_us,
        'events': events,
        'gallery_photos': gallery_photos,
    })

