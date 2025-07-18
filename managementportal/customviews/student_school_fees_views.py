from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from core.forms import DepartmentSchoolFeeForm, DepartmentFeeItemForm
from core.models import DepartmentSchoolFee, DepartmentFeeItem


from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# permission check
def is_custom_superuser(user):
    return user.is_authenticated and user.user_type == '1'


@login_required
@user_passes_test(is_custom_superuser)
def department_fee_item(request, department_fee_id ):
    department_fee = get_object_or_404(DepartmentSchoolFee, id=department_fee_id)
    fee_item = DepartmentFeeItem.objects.filter(
        department_school_fee=department_fee, #department_school_fee is the name we used to ref the model
    )
    context = {
        'fee_item': fee_item,
        'department_fee': department_fee
    }
    return render(request, 'management/partials/schoolfeespayment/department_fee_item.html', context)


@login_required
@user_passes_test(is_custom_superuser)
def manage_department_school_fees(request):
    department_fee = DepartmentSchoolFee.objects.all()
    context={
        'department_fee':department_fee
    }

    return render (request, 'management/partials/schoolfeespayment/manage_department_school_fees.html', context)



@login_required
@user_passes_test(is_custom_superuser)
def add_department_school_fees(request):
    form = DepartmentSchoolFeeForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        print('Form saved')
        messages.success(request, " Department  School fees created successfully ")
        return redirect(request.path)
    context={
        'form': form
    }

    return render (request, 'management/partials/schoolfeespayment/add_department_school_fees.html', context)


@login_required
@user_passes_test(is_custom_superuser)
def add_item_to_department_school_fee(request):

    form = DepartmentFeeItemForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        print("form saved")
        messages.success(request, " Item added to department school fees successfully ")
        return redirect(request.path)

    context={
        'form': form
    }
       
    return render (request, 'management/partials/schoolfeespayment/add_item_to_department_school_fee.html', context)