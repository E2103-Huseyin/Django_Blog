from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from .models import Profile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField() #EmailField(required=True)=EmailField() çünkü email 'in yazılmasını zorunlu hale gerirmek istiyoruz
    class Meta:
        model = User
        fields = ("username", "email") #UserCreationForm içerisinde email yoktu böylece eklemiş olduk
        
    #Custom validation yazacağız çünkü email unic mi kontrol etmek istiyoruz
    def clean_email(self): #clean_ yazmamız gerekli kural/methodu bu
        email = self.cleaned_data['email'] #.cleaned_data=>formun içerisindeki 'email' al
        if User.objects.filter(email=email).exists(): #email database'de var mı? email unic mi kontrol edilir
            raise forms.ValidationError("Plrase use another Email, That one already taken")
        return email
    
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("image", "bio")
                  
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email")


    
    