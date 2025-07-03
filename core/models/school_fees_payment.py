import uuid
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from core.models.enums import LevelChoices



def generate_reference():
    return str(uuid.uuid4()).replace('-', '')[:15]



class DepartmentSchoolFee(models.Model):
    department = models.ForeignKey('core.Department', on_delete=models.CASCADE)
    academic_calendar = models.ForeignKey('core.AcademicCalendar', on_delete=models.CASCADE)  
    level = models.CharField(max_length=3, choices=LevelChoices.choices)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    # def total_amount(self):
    #     return sum(item.amount for item in self.schoolfeeitem.all())
   
    def __str__(self):
        return self.department.name
    


    
class DepartmentFeeItem(models.Model):
    department_school_fee = models.ForeignKey('DepartmentSchoolFee', related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)  # e.g., Tuition, Medicals, ID card
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.title} - ₦{self.amount}"


from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

@receiver([post_save, post_delete], sender=DepartmentFeeItem)
def update_department_fee_total(sender, instance, **kwargs):
    department_fee = instance.department_school_fee
    total = department_fee.items.aggregate(total=models.Sum('amount'))['total'] or 0
    department_fee.total_amount = total
    department_fee.save()
    print("total amount updated")

class StudentSchoolFee(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey('core.Department', on_delete=models.CASCADE)
    level = models.CharField(max_length=10)
    academic_calendar = models.ForeignKey('core.AcademicCalendar', on_delete=models.CASCADE)  
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_paid = models.BooleanField(default=False)
    generated_at = models.DateTimeField(auto_now_add=True)

class SchoolFeeItem(models.Model):
    student_fee = models.ForeignKey('StudentSchoolFee', on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
