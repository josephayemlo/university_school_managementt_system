from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from ..models import AcademicCalendar
from ..forms import AcademicCalenderForm

# add
def add_academic_calender(request):
    form = AcademicCalenderForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Academic Calender added successfully.")
        return render(request, 'management/partials/success.html')
    return render(request, 'management/partials/add_academic_calender.html', {'form': form})


# manage/view
def manage_academic_calender(request):
    academic_calender = AcademicCalendar.objects.all()
    context= {"academic_calender":academic_calender}
    return render(request, 'management/partials/manage_academic_calender.html', context)

# edit
def edit_academic_calender(request, academic_calender_id):
    academic_calender = get_object_or_404(AcademicCalendar, id=academic_calender_id)
    if request.method == 'POST':
        form = AcademicCalenderForm(request.POST, instance=academic_calender)
        if form.is_valid():
            form.save()
            messages.success(request, 'Academic Calender Updated Sucessfully')
            return render(request,'management/partials/success.html')
    else:
        form = AcademicCalenderForm(instance=academic_calender)
    context = {
        "form": form,
        "academic_calender": academic_calender
    }
    return render(request, 'management/partials/edit_academic_calender.html', context)


