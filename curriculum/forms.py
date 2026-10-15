from django import forms

from curriculum.models import CurriculumItem


class CurriculumItemCreateForm(forms.ModelForm):
    class Meta:
        model = CurriculumItem
        fields = '__all__'

        labels = {
            'name': 'Form Name',
            'description': 'Description',
            'level': 'Level',
            'martial_art': 'Martial Art',
        }

        help_texts = {
            'level': 'Choose the curriculum level.',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Example: Siu Nim Tao',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Describe the form',
                }
            ),
        }