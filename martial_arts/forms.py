from django import forms
from django.core.exceptions import ValidationError

from martial_arts.models import MartialArt


class MartialArtBaseForm(forms.ModelForm):
    class Meta:
        model = MartialArt
        fields = '__all__'

        labels = {
            'name': 'Martial Art',
            'description': 'Description',
        }

        help_texts = {
            'name': 'Example: Wing Tsun, Karate, Tai Chi',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter martial art name',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Describe the martial art',
                }
            ),
        }

        error_messages = {
            'name': {
                'unique': 'This martial art already exists.',
            },
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if any(char.isdigit() for char in name):
            raise ValidationError(
                'Martial art name cannot contain numbers.'
            )

        return name


class MartialArtCreateForm(MartialArtBaseForm):
    ...


class MartialArtEditForm(MartialArtBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].disabled = True