from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterUser(UserCreationForm):
    email=forms.EmailField(required=True)
    first_name=forms.CharField(max_length=50,required=True)

    class Meta:
        model=User
        fields=('first_name','email','password1','password2')

    def save(self,commit=True):
        user=super(RegisterUser,self).save(commit=False)
        user.email=self.cleaned_data['email']
        user.username = self.cleaned_data['email']
        user.first_name=self.cleaned_data['first_name']
        

        if commit:
            user.save()

        return user