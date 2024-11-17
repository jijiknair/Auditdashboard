from django.contrib.auth.forms import AuthenticationForm
from .models import FacilityAuditnewfinal
from auditapp.models import FacilityAuditnewfinal
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')

        # Validate email format
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError("Invalid email address.")

        # Check if the email has the MOH domain
        if not email.endswith('@moh.gov.om'):
            raise ValidationError("Please use your MOH email (e.g., yourname@moh.gov.om) to sign up.")

        # Check if the email already exists in the database
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email address already in use.")

        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match.")

        return cleaned_data


class FacilityAuditForm(forms.ModelForm):
    class Meta:
        model = FacilityAuditnewfinal
        fields = [
            'governate', 'wilayat', 'facility_name',
            'head_of_institution', 'rationale', 'audit_date',
            'lead_auditor', 'auditors', 'areas_covered',
        ]


