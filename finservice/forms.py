from django import forms
from .models import ConsultationRequest, Service

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = ConsultationRequest
        fields = ["service", "name", "email", "mobile_number", "city_or_pincode", "whatsapp_opt_in"]
        widgets = {
            "service": forms.Select(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Your Name", "required": True}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Your Email", "required": True}),
            "mobile_number": forms.TextInput(attrs={"class": "form-control", "placeholder": "Your Phone Number", "required": True}),
            "city_or_pincode": forms.TextInput(attrs={"class": "form-control", "placeholder": "City or Pincode"}),
            "whatsapp_opt_in": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
