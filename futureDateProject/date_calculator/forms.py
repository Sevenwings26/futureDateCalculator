from django import forms

class DateCalculatorForm(forms.Form):
    days = forms.IntegerField(label='Enter the number of days:')
    