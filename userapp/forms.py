from django import forms
from .models import RegistrationModel,NewconnectionModel,RaisecomplaintsModel, ServicefeedbackModel

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = RegistrationModel
        fields ='__all__'

class NewconnectionForm(forms.ModelForm):
    class Meta:
        model = NewconnectionModel
        fields ='__all__'

class RaiseComplaintForm(forms.ModelForm):
    class Meta:
        model = RaisecomplaintsModel
        fields ='__all__'

class ServicefeedbackForm(forms.ModelForm):
    class Meta:
        model = ServicefeedbackModel
        fields ='__all__'