from django import forms
from .models import Cinema

class  Cinemaforms(forms.ModelForm):
    class Meta:
        model=Cinema
        fields=['name','desc','year','img']