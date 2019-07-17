from imagetagger.abml.models import ABMLExperiment
from django import forms


class ABMLExperimentCreationForm(forms.ModelForm):
    class Meta:
        model = ABMLExperiment
        fields = [
            'name',
            'description',
            'image_set',
            'recommender'
        ]
