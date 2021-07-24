from django import forms


class TokenAddFrom(forms.Form):
    token = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "*******",
                "class": "form-control"
            }
        )
    )