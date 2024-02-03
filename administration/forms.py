from django import forms 
from .models import program

class programform(forms.ModelForm):
    class Meta:
        model=program
        fields=['program_no','program_name','date','venue','discription','terms_condition','img']
