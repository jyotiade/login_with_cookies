from django import forms

class Registration(forms.Form):
    name=forms.CharField(max_length=30)
    email=forms.EmailField()
    city=forms.CharField(max_length=30)
    password=forms.IntegerField()

class Login(forms.Form):
    name=forms.CharField(max_length=40)
    email=forms.EmailField()
    password=forms.Field()