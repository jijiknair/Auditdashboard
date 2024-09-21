from django import forms
from django.contrib.auth.models import User
from .models import Appointment, Employeenew
from .models import UserProfile
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Meeting

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting  # Ensure this matches the model's name
        fields = ['room', 'date', 'start_time', 'end_time']
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=63)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'profile_image']


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employeenew
        fields = ['name', 'job_position']  # Include the new field


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['office_name', 'office_location', 'date', 'time']
    date = forms.DateField(widget=forms.DateInput(format='%m/%d/%Y', attrs={'placeholder': 'mm/dd/yyyy'}))
    time = forms.TimeField(widget=forms.TimeInput(format='%H:%M %p', attrs={'placeholder': '--:-- --'}))


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirmpassword = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username']

    def clean_confirmpassword(self):
        password = self.cleaned_data.get('password')
        confirmpassword = self.cleaned_data.get('confirmpassword')

        if password and confirmpassword and password != confirmpassword:
            raise forms.ValidationError("Passwords do not match!")

        return confirmpassword