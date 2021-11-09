from django import forms
from django.forms.models import ModelForm
from django.forms import Form #,widgets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserRegistrationform(UserCreationForm):

#overriding fields to add bootstrap class through Widget
   password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
   password2=forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
   email=forms.EmailField(required=True,label="Email",widget=forms.EmailInput(attrs={'class':'form-control'}))
   phone=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','autofocus':'','type':'tel','pattern':'[0-9]{10}'}))
   

#overriding password input's class of UserCreationForm and adding email field
   password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
   password2=forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
   email=forms.EmailField(required=True,label="Email",widget=forms.EmailInput(attrs={'class':'form-control'}))
  # test=forms.CharField(widget=forms.DateInput(attrs={'class':'form-control'}))

   class Meta:
      model=User
      #fields of models to use + explicitly declared fields  
      fields=['username','email','password1','password2']

     
 
      # to set field attributes for model fields which are generated automatically modelform

      widgets={'username':forms.TextInput(attrs={'class':'form-control'})}


class OtpForm(Form):

   
   input1=forms.CharField(max_length=1, label='',widget=forms.TextInput(attrs={'class':'form-control','autofocus':''}))
   input2=forms.CharField(max_length=1, label='',widget=forms.TextInput(attrs={'class':'form-control','autofocus':''}))
   input3=forms.CharField(max_length=1, label='',widget=forms.TextInput(attrs={'class':'form-control','autofocus':''}))
   input4=forms.CharField(max_length=1, label='',widget=forms.TextInput(attrs={'class':'form-control','autofocus':''}))

    input1=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','autofocus':''}))
    input2=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','autofocus':''}))
    input3=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','autofocus':''}))
    input4=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','autofocus':''}))


