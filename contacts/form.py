from django import forms

from .models import Contact


class AccountForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'role',
                  'phone', 'email', 'account',
                  )
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First name',
                    'class': 'form-control'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last name',
                    'class': 'form-control'
                }
            ),
            'role': forms.TextInput(
                attrs={
                    'placeholder': 'Role',
                    'class': 'gi-form-addr form-control'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Phone',
                    'class': 'form-control'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email',
                    'class': 'form-control'
                }
            )
            }
