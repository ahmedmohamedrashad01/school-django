from django import forms

class AddEmployee(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    address = forms.CharField(max_length=100, label="Address")
    age = forms.IntegerField(max_value=30,min_value=6, label='Age')
    studentclass = forms.IntegerField(min_value=1, max_value=15, label='Student Class')


class EditEmployee(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    address = forms.CharField(max_length=100, label="Address")
    age = forms.IntegerField(max_value=30,min_value=6, label='Age')
    studentclass = forms.IntegerField(min_value=1, max_value=15, label='Student Class')
