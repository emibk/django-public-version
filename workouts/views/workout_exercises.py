from django.shortcuts import get_object_or_404, render
from django.views import generic

from workouts.models import Workout, WorkoutDay, WorkoutDayExercise, Exercise, Progress


def workout_exercises(request, workout_day_id, workout_id):
    workout = get_object_or_404(Workout, pk=workout_id)
    workout_day = get_object_or_404(WorkoutDay, pk=workout_day_id)
    workout_exercises_ = WorkoutDayExercise.objects.filter(workout_day=workout_day)
    
    return render(request, 'workouts/workout_exercises.html',
                  {'workout': workout, 'workout_day': workout_day, 'workout_exercises': workout_exercises_, 'workout_day_id': workout_day_id,
     })
