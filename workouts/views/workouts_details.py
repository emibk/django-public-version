from django.shortcuts import get_object_or_404, render
from django.views import generic

from workouts.models import Workout, WorkoutDay, WorkoutDayExercise, Exercise


def workout_details(request, workout_id):
    workout_ = get_object_or_404(Workout, pk=workout_id)
    workout_days = WorkoutDay.objects.filter(workout=workout_)

    return render(request, 'workouts/workout_details.html', {'workout': workout_, 'workout_days': workout_days})
