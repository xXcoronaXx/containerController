from django import forms

class ContainerForm(forms.Form):
    id_container = forms.CharField(label='Container', max_length=50)
    text = forms.CharField(label='Description',widget=forms.Textarea)