from celery import shared_task
from django.core.mail import send_mail
from core.models import AspirantStudent 
from django.conf import settings

# aspirants tasks
@shared_task
def send_reminder(aspirant_id):
    try:
        aspirant = AspirantStudent.objects.get(id=aspirant_id)
        send_mail(
            subject="Complete Application",
            message=f"Hi {aspirant.admin.first_name}, it's been a week since you registered, ensure to complete your application else your application will not be considered for admission.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[aspirant.admin.email]
        )
        print(f"✅ Email sent to {aspirant.admin.email}")
    except AspirantStudent.DoesNotExist:
        print(f"❌ Aspirant with ID {aspirant_id} not found.")
