from django.shortcuts import render, redirect, get_object_or_404
from workouts.forms import DisabilityForm, DisabilityDeleteForm
from workouts.models import Disability

def disability_list(request):
    disabilities = Disability.objects.all()
    delete_form = DisabilityDeleteForm()
    form = DisabilityForm()
    
    if request.method == 'POST':
        if 'delete-goal' in request.POST:
            delete_form = DisabilityDeleteForm(request.POST)
            if delete_form.is_valid():
                disability_id = delete_form.cleaned_data['disability_id']
                disability = get_object_or_404(Disability, pk=disability_id)
                disability.delete()
                return redirect(request.path) 
        else:
            form = DisabilityForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(request.path)  
    else:
        form = DisabilityForm()
        delete_form = DisabilityDeleteForm()

    return render(request, 'admin_templates/disabilities.html', {'disabilities': disabilities, 'form': form, 'delete_form': delete_form})
