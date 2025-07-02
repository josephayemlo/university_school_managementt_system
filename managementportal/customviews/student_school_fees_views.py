from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from core.forms import DepartmentSchoolFeeForm, DepartmentFeeItemForm




def add_department_school_fees(request):
    form = DepartmentSchoolFeeForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save
        messages.success(request, " Department  School fees created successfully ")
        return render(request, 'management/partials/success.html')
    context={
        'form': form
    }

    return render (request, 'management/partials/schoolfeespayment/add_department_school_fees.html', context)



def add_item_to_department_school_fee(request):

    form = DepartmentFeeItemForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        print("form saved")
        messages.success(request, " Item added to department school fees successfully ")
        return render(request, 'management/partials/success.html')
    context={
        'form': form
    }
       
    return render (request, 'management/partials/schoolfeespayment/add_item_to_department_school_fee.html', context)