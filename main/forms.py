from django import forms

from .models import Children, Presences


class ChildrenAddForm(forms.Form):
    first_name = forms.CharField(
        max_length=64,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Imię'
            }
        )
    )
    last_name = forms.CharField(
        max_length=256,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nazwisko'
            }
        )
    )


class ChildrenPresenceForm(forms.Form):
    children = forms.ModelChoiceField(queryset=Children.objects.all())
    data_start = forms.DateTimeField()
    data_end = forms.DateTimeField()
    presence = forms.BooleanField()
