from django import forms
from .models import *
from django.contrib.auth.models import User

class beneficiary_info(forms.ModelForm):
    class Meta:
        model = beneficiary_register
        fields = ('u_fname','u_sname','u_adhar','u_addr','u_pincode','u_phno','u_district','u_status','u_verified')
   
       
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password')
        
class usr(forms.ModelForm):
    class Meta:
        model = userbmi
        fields = '__all__'
        widgets = {'currentbmi': forms.HiddenInput(),'bmworker': forms.HiddenInput()} 