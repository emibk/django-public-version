from workouts.forms import CaloriesForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from workouts.models import FoodCalories
from django.db.models import Sum
from django.core.paginator import Paginator

@login_required
@user_passes_test(lambda user: user.groups.filter(name='Platitor').exists())
def calories_intake(request):
    
    calories_list = FoodCalories.objects.filter(user=request.user).order_by('-date')
    calories_dates = calories_list.values('date').distinct()
    calorie_entries = []

    for date in calories_dates:
        entry = {}
        foods = FoodCalories.objects.filter(user=request.user, date=date['date']).values('food', 'calories', 'meal_type')
        entry['foods'] = foods
        entry['date'] = date['date']
        entry['total_calories'] = foods.aggregate(Sum('calories'))['calories__sum']
        calorie_entries.append(entry)
    calorie_entries = calorie_entries[:70]
    

    if request.method == 'POST':
        form = CaloriesForm(request.POST)
        if form.is_valid():
            food_calories= form.save(commit=False)
            food_calories.user = request.user
            food_calories.save()
            return redirect('/calories')  
    else:
        form = CaloriesForm()
    print(calories_dates)
    return render(request, 'calories/calories_intake.html', {'form': form, 
                                                             'calories_list': calories_list,
                                                             'calories_dates':calories_dates,
                                                             'calorie_entries': calorie_entries,
                                                           
                                                            
                                                             })
