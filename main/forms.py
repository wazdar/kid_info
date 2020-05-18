from django import forms

from .models import Children, Presences


class ChildrenAddForm(forms.ModelForm):
    class Meta:
        model = Children
        fields = ['first_name', 'last_name']


class ChildrenPresenceForm(forms.Form):
    children = forms.ModelChoiceField(queryset=Children.objects.all())
    data_start = forms.DateTimeField()
    data_end = forms.DateTimeField()
    presence = forms.BooleanField()
