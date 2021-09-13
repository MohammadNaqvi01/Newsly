from django.http.response import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from django.views import View
from .forms import *
# Create your views here



def home(request):
    
    context={
        'greet':'Welcome',
        'name':'Newsly'
        
    }

    return render(request,'trail/home.htm',context)
   
   #  return render(request,'home.html')




class SignUp(View):
    def get(self,request):
        form=UserRegistrationform()
        return render(request,'trail/signup.htm',{'form':form})
    def post(self,request):

        form=UserRegistrationform(request.POST)
        if form.is_valid():

          print(request.POST)
          
          form.save()
          return HttpResponseRedirect('/login/')
        else:
          return render(request,'trail/signup.htm',{'form':form})
class Otp(View):
    def get(self,request):
        form=OtpForm()
        return render(request,'trail/login.htm',{'form':form})

