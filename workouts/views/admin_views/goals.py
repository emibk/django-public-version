from django.shortcuts import render, redirect, get_object_or_404
from workouts.forms import GoalForm, GoalDeleteForm
from workouts.models import Goal

def goal_list(request):
    goals = Goal.objects.all()
    delete_form = GoalDeleteForm()
    form = GoalForm()
    
    if request.method == 'POST':
        if 'delete-goal' in request.POST:
            delete_form = GoalDeleteForm(request.POST)
            if delete_form.is_valid():
                goal_id = delete_form.cleaned_data['goal_id']
                goal = get_object_or_404(Goal, pk=goal_id)
                goal.delete()
                return redirect(request.path) 
        else:
            form = GoalForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(request.path)  
    else:
        form = GoalForm()
        delete_form = GoalDeleteForm()

    return render(request, 'admin_templates/goals.html', {'goals': goals, 'form': form, 'delete_form': delete_form})
