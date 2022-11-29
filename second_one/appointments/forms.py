from django.forms import ModelForm
from .models import User, Appointment

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'last_name', 'email', 'date_of_birth']
        
class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        # widgets = 