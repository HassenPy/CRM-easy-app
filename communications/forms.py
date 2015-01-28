from django import forms

from .models import Communication


class CommunicationForm(forms.Modelform):
    class Meta:

        model = Communication
        fields = ('subject', 'notes', 'kind', 'date', 'account')
        widgets = {
            'subject': forms.TextInpt(
                attrs={'placeholder': 'Subject',
                       'class': 'form-control'
                       }
            ),
            'notes': forms.Textarea(
                attrs={'placeholder': 'Notes',
                       'class': 'form-control'
                       }
            ),
            'kind': forms.Select(
                attrs={'placeholder': 'Type',
                       'class': 'form-control'
                       }
            ),
            'date': forms.DateInput(
                attrs={'placeholder': 'Date',
                       'class': 'form-control'
                       }
            ),
        }
