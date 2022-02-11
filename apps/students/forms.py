from django import forms

from .models import students
from apps.parents.models import parents


class createStudent(forms.ModelForm):
    # name: forms.CharField(label='Name', max_length=100, widget=forms.TextInput(
        # attrs={'class': 'form-control', 'placeholder': 'Enter name'}))
    # family: forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter name'}))
    # parent = forms.ModelChoiceField(queryset=parents.objects.filter(name='حسین'))

    class Meta:
        model = students
        fields = ('name', 'family', 'parent')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Name'})
        self.fields['family'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Name'})
        self.fields['parent'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Name'})
