from django.db import models
from django.contrib.auth.models import User

class Staff(models.Model):
    '''Bu yerda Stafflarning nodeli yozilgan'''
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    tel_num = models.CharField(max_length=13, null=True)
    email = models.EmailField(max_length=255)

    

    class Meta:
        verbose_name_plural = 'Staffs'
        verbose_name = 'Staff'



class Attendance(models.Model):
    
    come_date = models.DateField(auto_now_add=True)
    back_date = models.DateField(blank=True,null=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.staff.f_name} {self.staff.l_name} {self.staff.status} {self.staff.tel_num} {self.staff.email}'


 




# Create your models here.



























