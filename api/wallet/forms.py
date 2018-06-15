from django import forms


class TransferForm(forms.Form):
    num = forms.FloatField(required=True)
    receive = forms.CharField(max_length=15, min_length=15, required=True)


class ExtractForm(forms.Form):
    num = forms.FloatField(required=True)
