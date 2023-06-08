from django.shortcuts import render, redirect, get_object_or_404
from workouts.forms import WorkoutDeleteForm, WorkoutForm, WorkoutDayExerciseDeleteForm, WorkoutDayExerciseForm
from workouts.models import Workout, WorkoutDay, WorkoutDayExercise
from django.core.paginator import Paginator

def workoutadmin_list(request):
    workouts = Workout.objects.all()
    delete_form = WorkoutDeleteForm()
    form = WorkoutForm()
    name = request.GET.get('name')
    if name and name != 'None':
        workouts = workouts.filter(name__icontains=name)
    if request.method == 'POST':
        if 'delete-goal' in request.POST:
            delete_form = WorkoutDeleteForm(request.POST)
            if delete_form.is_valid():
                workout_id = delete_form.cleaned_data['workout_id']
                workout = get_object_or_404(Workout, pk=workout_id)
                workout.delete()
                return redirect(request.path) 
        else:
            form = WorkoutForm(request.POST, request.FILES)
            if form.is_valid():
                workout = form.save()
                length = form.cleaned_data['length']
                for day_number in range(1, length + 1):
                    workout_day = WorkoutDay(day=day_number, workout=workout)
                    workout_day.save()
                return redirect(request.path)  
    else:
        form = WorkoutForm()
        delete_form = WorkoutDeleteForm()

    return render(request, 'admin_templates/workouts.html', {'workouts': workouts, 'form': form, 'delete_form': delete_form,
                                                             'name':name})

from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

def workoutplan_list(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id)
    workout_days = WorkoutDay.objects.filter(workout=workout)
    exercise_form = WorkoutDayExerciseForm()
    delete_form = WorkoutDayExerciseDeleteForm()
    paginator = Paginator(workout_days, 2)
    page_number = request.GET.get('page')
    workout_days = paginator.get_page(page_number)

    if request.method == 'POST':
        if 'add-exercise' in request.POST:
            exercise_form = WorkoutDayExerciseForm(request.POST)
            if exercise_form.is_valid():
                exercise = exercise_form.save(commit=False)
                workout_day_id = request.POST.get('workout_day_id')
                workout_day = get_object_or_404(WorkoutDay, id=workout_day_id)
                exercise.workout_day = workout_day
                exercise.save()
                return redirect('workout-days', workout_id=workout_id)
            

        elif 'delete-exercise' in request.POST:
            delete_form = WorkoutDayExerciseDeleteForm(request.POST)
            if delete_form.is_valid():
                workoutexercise_id = delete_form.cleaned_data['workoutexercise_id']
                workoutexercise = get_object_or_404(WorkoutDayExercise, id=workoutexercise_id)
                workoutexercise.delete()
                return redirect('workout-days', workout_id=workout_id)

    return render(request, 'admin_templates/workout_plan.html', {
        'workout': workout,
        'workout_days': workout_days,
        'exercise_form': exercise_form,
        'delete_form': delete_form,
        'page_obj': workout_days,
    })
