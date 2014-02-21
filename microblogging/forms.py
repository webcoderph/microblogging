from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    last_name = forms.CharField(required=True)
    first_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username','last_name','first_name','email', 'password1', 'password2')
        
    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        # user.set_password(self.cleaned_data['password1'])
        
        if commit:
            user.save()
            
        return user