from django.shortcuts import render, redirect,  get_object_or_404
from accounts.forms import NonAcademicStaffForm, CustomUser 
from django.contrib import messages
from accounts.models import CustomUser, NonAcademicStaff
from django.urls import reverse

# Create your views here.

def add_nonacademicstaff(request):
    form = NonAcademicStaffForm(request.POST or None, request.FILES or None)
    context = {'form': form, 'page_title': 'Add NonAcademic Staff'}
    if request.method == 'POST':
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            address = form.cleaned_data.get('address')
            email = form.cleaned_data.get('email')
            gender = form.cleaned_data.get('gender')
            password = form.cleaned_data.get('password')
        
            try:
                user = CustomUser.objects.create_user(
                    email=email, password=password, user_type=3, first_name=first_name, last_name=last_name)
                user.gender = gender
                user.address = address
                user.save()
                messages.success(request, "NonAcademic Staff Successfully Added")
                return redirect('management_home')

            except Exception as e:
                messages.error(request, "Could Not Add " + str(e))
        else:
            messages.error(request, "Please fulfil all requirements")

    return render(request, 'add_nonacademicstaff_template.html', context)


def nonacademicstaff_list(request):
    nonacademicstaffs = CustomUser.objects.filter(user_type=3)
    return render(request, 'staff/nonacademicstaff_list.html', {'nonacademicstaffs': nonacademicstaffs})

def edit_nonacademicstaff(request, nonacademicstaff_id):
    nonacademicstaff = get_object_or_404(NonAcademicStaff, id=nonacademicstaff_id)
    form = NonAcademicStaffForm(request.POST or None, instance=nonacademicstaff)
    context = {
        'form': form,
        'nonacademicstaff_id': nonacademicstaff_id,
        'page_title': 'Edit Academic Staff'
    }
    if request.method == 'POST':
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            address = form.cleaned_data.get('address')
            email = form.cleaned_data.get('email')
            gender = form.cleaned_data.get('gender')
            password = form.cleaned_data.get('password') or None
            try:
                user = CustomUser.objects.get(id=nonacademicstaff.admin.id)                
                user.email = email
                if password != None:
                    user.set_password(password)
                user.first_name = first_name
                user.last_name = last_name
                user.gender = gender
                user.address = address
                user.save()
                nonacademicstaff.save()
                messages.success(request, "Successfully Updated")
                return redirect(reverse('edit_nonacademicstaff', args=[nonacademicstaff_id]))
            except Exception as e:
                messages.error(request, "Could Not Update " + str(e))
        else:
            messages.error(request, "Please Fill Form Properly!")
    else:
        return render(request, "management/edit_nonacademicstaff_template.html", context)


def delete_nonacademicstaff(request, nonacademicstaff_id):
    nonacademicstaff = get_object_or_404(CustomUser, nonacademicstaff__id=nonacademicstaff_id)
    nonacademicstaff.delete()
    messages.success(request, "nonacademicstaff deleted successfully!")
    return redirect(reverse('nonacademicstaff_list'))

