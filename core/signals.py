from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Student
from core.models import AspirantStudent
from django.core.mail import send_mail
from django.conf import settings
import random

# Step 1: Capture the previous status before saving
@receiver(pre_save, sender=AspirantStudent)
def cache_old_status(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            instance._previous_admission_status = old_instance.admission_status
        except sender.DoesNotExist:
            instance._previous_admission_status = None
    else:
        instance._previous_admission_status = None


# Step 2: On save, check if status changed to 'admitted' and act
@receiver(post_save, sender=AspirantStudent)
def handle_admission_status_change(sender, instance, created, **kwargs):
    print('✅ signal loaded')

    if created:
        return

    if getattr(instance, '_previous_admission_status', None) != instance.admission_status and instance.admission_status == 'admitted':
        print("✅ admission status changed to 'admitted'")

        user = instance.admin

        # Update user_type to '4' (Student)
        user.user_type = '4'
        user.save()
        print("✅ user_type updated to student")

        # Create student profile if it doesn't exist yet
        """
        leaving the matric number field empty will result it unique contraint issue
        because from the student model the field is unique thus we cant have two 
        empty matric number field

        what we will do later here, create a course addmitted field in the aspirant model
        get the course from here then dynamically assign matric number from here based on course and department
        """

        custom_matric = "CSA/2025/"+ str(random.randint(2001, 2002))

        if not hasattr(user, 'student'):
            Student.objects.create(admin=user, matric_no =custom_matric)
            print("✅ student profile created")

        # Send confirmation email
        try:
            send_mail(
                subject="🎉 Admission Successful – Student Portal Access",
                message=f"""
Dear {user.first_name},

Congratulations! Your admission has been approved.

You are now officially a student.

Login Email: {user.email}
(Use the same password you created during application)

Login here to continue: https://yourdomain.com/login/

Regards,  
Admissions Office
""",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False,
            )
            print("✅ email sent successfully")
        except Exception as e:
            print(f"❌ email sending failed: {e}")
