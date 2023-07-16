from django import forms


class register(forms.Form):
    first_name=forms.CharField(label='first_name',max_length=40,required=True)
    last_name=forms.CharField(label='last_name',max_length=40,required=True)
    user_name=forms.CharField(label='user_name',max_length=40,required=True)
    email=forms.EmailField(label='email',max_length=50,required=True)
    password1 = forms.CharField(
    help_text='Enter Password',
    required = True,
    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
    required = True,
    help_text='Enter Password Again',
    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),
    )

class loginform(forms.Form):
    user_name=forms.CharField(label='user_name',max_length=50,help_text='enter user_name',required=True)
    password=forms.CharField(required=True,help_text='enter password',widget=forms.PasswordInput(attrs={'placeholder':'password'}))