from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from workouts.models import Progress
from workouts.forms import ProgressForm
from workouts.models import WorkoutDay
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group

@login_required
@user_passes_test(lambda user: user.groups.filter(name='Utilizator').exists())
def add_progress(request, workout_day_id, workout_id):
    workout_day = get_object_or_404(WorkoutDay, pk=workout_day_id)
    print(workout_day)
    if request.method == 'POST':
        print("POST request received")
        form = ProgressForm(request.POST)
        if form.is_valid():
            progress = form.save(commit=False)
            progress.user = request.user
            progress.workout_day = workout_day
            progress.save()
            print("Progress saved")
            return redirect('/workouts/'+str(workout_id))
        else:
            print("Invalid form")
    else:
        form = ProgressForm(initial={'user': request.user, 'workout_day': workout_day})
    return render(request, 'workouts/workout_exercises.html', {'form': form})
