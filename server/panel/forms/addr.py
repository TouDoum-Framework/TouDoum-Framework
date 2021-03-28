from django import forms


class AddAddrForm(forms.Form):
    ips = forms.CharField(required=True)
    priority = forms.IntegerField(initial=0, required=True)
