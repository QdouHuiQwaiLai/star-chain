from django import forms


class PromoteForm(forms.Form):
    num = forms.IntegerField(required=True)