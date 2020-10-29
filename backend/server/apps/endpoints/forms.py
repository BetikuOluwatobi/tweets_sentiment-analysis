from django import forms

class PredictForm(forms.Form):
  text = forms.CharField(max_length=300)