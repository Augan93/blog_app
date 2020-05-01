from django import forms


class LoginForm(forms.Form):
    login = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Email...',
                'class': 'InputElement',
            }
        )
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password...',
                'class': 'InputElement'
            }
        ),
    )
