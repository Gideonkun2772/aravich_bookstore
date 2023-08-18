from django import forms


class registerform(forms.Form):
    username=forms.CharField(label='username',max_length=40,required=True)
    email=forms.EmailField(label='email',max_length=50,required=True)
    password1 = forms.CharField(
    required = True,
    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
    required = True,
    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),
    )

class loginform(forms.Form):
    username=forms.CharField(label='username',max_length=50,widget=forms.TextInput(attrs={'placeholder':'enter username'}),required=True)
    password=forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder':'enter password'}))

