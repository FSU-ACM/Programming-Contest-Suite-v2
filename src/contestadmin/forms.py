from django import forms
from django.contrib.auth.models import User
from django.contrib.admin.widgets import FilteredSelectMultiple

from contestadmin.models import Contest

class GenerateWalkinForm(forms.Form):
    DIVISION = (
        (1, 'Upper Division'),
        (2, 'Lower Division')
    )

    total = forms.IntegerField()
    division = forms.ChoiceField(choices=DIVISION)


class ResultsForm(forms.ModelForm):
    class Meta:
        model = Contest
        fields = ['results']
