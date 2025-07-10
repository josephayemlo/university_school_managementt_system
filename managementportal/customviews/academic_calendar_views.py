from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from ..forms import AcademicCalenderForm, AspirantAcademicCalendarForm
from core.models import AcademicCalendar, AspirantAcademicCalendar



# add
def add_academic_calender(request):
    form = AcademicCalenderForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Academic Calender added successfully.")
        return render(request, 'management/partials/success.html')
    return render(request, 'management/partials/academiccalender/add_academic_calender.html', {'form': form})


# manage/view
def manage_academic_calender(request):
    academic_calender = AcademicCalendar.objects.all()
    context= {"academic_calender":academic_calender}
    return render(request, 'management/partials/academiccalender/manage_academic_calender.html', context)

# edit
def edit_academic_calender(request, academic_calender_id):
    academic_calender = get_object_or_404(AcademicCalendar, id=academic_calender_id)
    if request.method == 'POST':
        form = AcademicCalenderForm(request.POST, instance=academic_calender)
        if form.is_valid():
            form.save()
            messages.success(request, 'Academic Calender Updated Sucessfully')
            return redirect(request.path)
    else:
        form = AcademicCalenderForm(instance=academic_calender)
    context = {
        "form": form,
        "academic_calender": academic_calender
    }
    return render(request, 'management/partials/academiccalender/edit_academic_calender.html', context)


# AsprantAcademicCalender
# add
def add_aspirant_academic_calender(request):
    form = AspirantAcademicCalendarForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Academic Calender added successfully.")
        return render(request, 'management/partials/success.html')
    return render(request, 'management/partials/academiccalender/add_aspirant_academic_calender.html', {'form': form})


# manage/view
def manage_aspirant_academic_calender(request):
    aspirant_academic_calender = AspirantAcademicCalendar.objects.all()
    context= {"aspirant_academic_calender":aspirant_academic_calender}
    return render(request, 'management/partials/academiccalender/manage_aspirant_academic_calender.html', context)

# edit
def edit_aspirant_academic_calender(request, aspirant_academic_calender_id):
    aspirant_academic_calender = get_object_or_404(AspirantAcademicCalendar, id=aspirant_academic_calender_id)
    if request.method == 'POST':
        form = AspirantAcademicCalendarForm(request.POST, instance=aspirant_academic_calender)
        if form.is_valid():
            form.save()
            messages.success(request, 'Academic Calender Updated Sucessfully')
            return redirect(request.path)
    else:
        form = AspirantAcademicCalendarForm(instance=aspirant_academic_calender)
    context = {
        "form": form,
        "aspirant_academic_calender": aspirant_academic_calender
    }
    return render(request, 'management/partials/academiccalender/edit_aspirant_academic_calender.html', context)


