from django.shortcuts import render, redirect,  get_object_or_404
from core.forms import NonAcademicStaffForm 
from django.contrib import messages
from core.models import NonAcademicStaff
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# permission check
def is_custom_superuser(user):
    return user.is_authenticated and user.user_type == '1'



# add academic staff
@login_required
@user_passes_test(is_custom_superuser)
def add_nonacademicstaff(request):
    form = NonAcademicStaffForm(request.POST or None, request.FILES or None)
    context = {'form': form, 'page_title': 'Add NonAcademicStaff'}

    if request.method == 'POST':
        if form.is_valid():
            # User fields
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            address = form.cleaned_data.get('address')
            email = form.cleaned_data.get('email')
            gender = form.cleaned_data.get('gender')
            password = form.cleaned_data.get('password')

            # Extra fields
            role = form.cleaned_data.get('role')


            try:
                # Create user with all fields at once
                user = User.objects.create_user(
                    email=email,
                    password=password,
                    user_type=3,
                    first_name=first_name,
                    last_name=last_name,
                    gender=gender,
                    address=address
                )
                # Manually create Academicstaff object
                nonacademicstaff = NonAcademicStaff.objects.create(
                    admin=user,
                    role=role,
                )
                messages.success(request, "Staff successfully added.")
                return redirect(request.path) 
            except Exception as e:
                messages.error(request, "Could not add Staff: " + str(e))
        else:
            messages.error(request, "Please fill all required fields correctly.")
    return render(request, 'management/partials/nonacademicstaff/add_nonacademicstaff.html', context)



# list
@login_required
@user_passes_test(is_custom_superuser)
def manage_nonacademicstaff(request):
    nonacademicstaff = NonAcademicStaff.objects.select_related('admin').order_by('admin__last_name')
    return render(request, 'management/partials/nonacademicstaff/manage_nonacademicstaff.html', {'nonacademicstaff': nonacademicstaff})

# edit
@login_required
@user_passes_test(is_custom_superuser)
def edit_nonacademicstaff(request, nonacademicstaff_id):
    nonacademicstaff = get_object_or_404(NonAcademicStaff, id=nonacademicstaff_id)
    user = nonacademicstaff.admin  # linked User object
    form = NonAcademicStaffForm(request.POST or None, instance=nonacademicstaff)

    if request.method == 'POST':
        if form.is_valid():
            try:
                # Update User fields
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.email = form.cleaned_data['email']
                user.address = form.cleaned_data['address']
                user.gender = form.cleaned_data['gender']
                
                password = form.cleaned_data.get('password')
                if password:
                    user.set_password(password)
                user.save()

                # Update Student fields
                nonacademicstaff.role = form.cleaned_data['role']
                nonacademicstaff.save()

                messages.success(request, "Successfully updated Staff.")
                return redirect(request.path)
            
            except Exception as e:
                messages.error(request, f"Could not update Staff: {e}")
        else:
            messages.error(request, "Please fill out the form correctly.")

    context = {
        'form': form,
        'nonacademicstaff': nonacademicstaff,
    }
    return render(request, "management/partials/nonacademicstaff/edit_nonacademicstaff.html", context)

# delete
@login_required
@user_passes_test(is_custom_superuser)
def delete_nonacademicstaff(request, nonacademicstaff_id):
    if request.method == 'POST':
        nonacademicstaff = get_object_or_404(NonAcademicStaff, id=nonacademicstaff_id)
        nonacademicstaff.delete()
        print("nonacademicstaff deleted")
        messages.success(request, 'nonacademicstaff Deleted Sucessfully')
        return render(request,'management/partials/success.html')
    return render(request, 'management/partials/nonacademicstaff/manage_nonacademicstaff.html')
    