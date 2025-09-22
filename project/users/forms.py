
    
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from users import models
class RegisterForm(UserCreationForm):
    class Meta:
        model = models.User         
        fields = ['name', 'email', 'phone' , 'password1' , 'password2' , 'role' ]
        widgets = {
            'name': forms.TextInput(attrs={'autocomplete': 'off'}),
            'email': forms.EmailInput(attrs={'autocomplete': 'off'}),
            'password': forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
            'phone': forms.TextInput(attrs={'autocomplete': 'off'}),
        }



from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    email = forms.EmailField(
        max_length=254, 
        widget=forms.EmailInput(attrs={"placeholder": "Email"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError("Invalid email or password")
            cleaned_data["user"] = user
        return cleaned_data