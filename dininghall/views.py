from django.shortcuts import render

from .models import Meals, Hall, MealCount

def homepage(request):
    meals = Meals.objects.order_by('name')
    return render(request, 'reports/index.html', {'meals': meals})
