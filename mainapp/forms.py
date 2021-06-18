from django import forms
from .models import *

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields =('name','directory','cast','description','release_date','avaragerating','image')
        


 