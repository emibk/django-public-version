from django.shortcuts import render
from django.views import generic

from workouts.models import Workout, Goal, Disability


def workout_list(request):
    workouts = Workout.objects.all()
    goal = request.GET.get('goal')
    disability = request.GET.get('disability')
    goal_options = Goal.objects.all()
    disability_options = Disability.objects.all()

    if goal:
        workouts = workouts.filter(goal=goal)
    if disability:
        workouts = workouts.filter(disability=disability)

    context = {
        'workout_list': workouts,
        'goal': goal,
        'disability': disability,
        'goal_options': goal_options,
        'disability_options': disability_options,
    }
    print(context)
    return render(request, 'workouts/workout_list.html', context)

