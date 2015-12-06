from django.shortcuts import render

from .models import Meals, Hall

def homepage(request):
    halls = Hall.objects.order_by('name')
    return render(request, 'meals/index.html', {'halls': halls})

def halldetail(request, hall_slug):
    dorm = Hall.objects.get(name_slug=hall_slug)
    meals = Meals.objects.filter(hall=dorm).order_by('-total')
    return render(request, 'meals/halldetail.html', {'dorm': dorm, 'meals': meals})

