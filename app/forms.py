from django import forms

class CreateMatchForm(forms.Form):
    username1 = forms.CharField(label='Username 1', max_length=50)
    username2 = forms.CharField(label='Username 2', max_length=50)
    phone1 = forms.IntegerField(label='Phone 1')
    phone2 = forms.IntegerField(label='Phone 2')