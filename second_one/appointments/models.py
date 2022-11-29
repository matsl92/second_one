from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.IntegerField(unique=True)
    password = models.CharField(max_length=40)
    
    def __str__(self):
        return str(self.phone_number)
    
# class CustomUser(AbstractUser):
#     phone_number = models.IntegerField(unique=True, null=True, blank=True)  # uncoment the AUTH element in the settings file

class Gap(models.Model):
    date_and_time = models.DateTimeField(unique=True)
    time_period = models.DurationField()
    index = models.CharField(max_length=10, default='')
    
    def __str__(self):
        return str(self.date_and_time.time())
    
class Appointment(models.Model):
    gap = models.OneToOneField(Gap, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.gap

# class Appointment(models.Model):
#     gap = models.OneToOneField(Gap, on_delete=models.CASCADE)
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.gap

class Week(models.Model):
    minutes_per_appointment = models.IntegerField(default=30)
    start_date = models.DateField(default=timezone.now)
    monday_start = models.TimeField(default=datetime.time(7), blank=True, null=True)
    monday_end = models.TimeField(default=datetime.time(22), blank=True, null=True)
    tuesday_start = models.TimeField(default=datetime.time(7), blank=True, null=True)
    tuesday_end = models.TimeField(default=datetime.time(22), blank=True, null=True)
    wednesday_start = models.TimeField(default=datetime.time(7), blank=True, null=True)
    wednesday_end = models.TimeField(default=datetime.time(22), blank=True, null=True)
    thursday_start = models.TimeField(default=datetime.time(7), blank=True, null=True)
    thursday_end = models.TimeField(default=datetime.time(22), blank=True, null=True)
    friday_start = models.TimeField(default=datetime.time(7), blank=True, null=True)
    friday_end = models.TimeField(default=datetime.time(22), blank=True, null=True)
    saturday_start = models.TimeField(default=datetime.time(7), blank=True, null=True)
    saturday_end = models.TimeField(default=datetime.time(22), blank=True, null=True)
    sunday_start = models.TimeField(default=datetime.time(7), blank=True, null=True)
    sunday_end = models.TimeField(default=datetime.time(22), blank=True, null=True)
