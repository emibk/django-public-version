from django.shortcuts import render, redirect, get_object_or_404
from workouts.forms import ExerciseForm, ExerciseDeleteForm
from workouts.models import Exercise

def exercise_list(request):
    exercises = Exercise.objects.all()
    delete_form = ExerciseDeleteForm()
    form = ExerciseForm()
    name = request.GET.get('name')
    muscle_group = request.GET.get('muscle_group')
    if name and name != 'None':
        exercises = exercises.filter(name__icontains=name)
    if muscle_group and muscle_group != 'None':
        exercises = exercises.filter(muscle_group__icontains=muscle_group)
   
    if request.method == 'POST':
        if 'delete-goal' in request.POST:
            delete_form = ExerciseDeleteForm(request.POST)
            if delete_form.is_valid():
                exercise_id = delete_form.cleaned_data['exercise_id']
                exercise = get_object_or_404(Exercise, pk=exercise_id)
                exercise.delete()
                return redirect(request.path) 
        else:
            form = ExerciseForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(request.path)  
    else:
        form = ExerciseForm()
        delete_form = ExerciseDeleteForm()

    return render(request, 'admin_templates/exercises.html',
                   {'exercises': exercises, 'form': form, 'delete_form': delete_form,
                    'name':name, 'muscle_group': muscle_group})
