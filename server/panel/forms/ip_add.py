from django import forms


class IpAddFrom(forms.Form):
    ip_range = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "xxx.xxx.xxx.xxx/xx",
                "class": "form-control"
            }
        )
    )
    rescan_priority = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "0",
                "class": "form-control"
            }
        )
    )
