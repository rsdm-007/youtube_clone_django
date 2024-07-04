from django import forms
#from .models import videos,channel,uploadmod
class barform(forms.Form):
    bar=forms.CharField(max_length=50,label="",widget=forms.TextInput(attrs={'class':'input','placeholder':('SEARCH'),'style': 'border: 5px solid black;',}))