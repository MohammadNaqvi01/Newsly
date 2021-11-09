
from django.contrib.auth import authenticate,login
from django.contrib import messages
from app.models import OtpModel
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.core.cache import cache


from django.http.response import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from django.views import View
from .forms import *

import random
# Create your views here

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)



def get_db():
  
    # string="checking redis"
    # TestModel(text=string).save()
    
    # text=TestModel.objects.all()
    # print(text)
    
    # print("##########Full Db Called#########")
    text='booooooooo'
    return text





#@cache_page(CACHE_TTL)
def check(request):
    context=request.session['check']

    
    messages.success(request,f'Boooo! Just kidding {context}')
    return render(request,'trail/check.htm')
   
   # return render(request,'home.html')


# Create your views here




# Create your views here




def home(request):
    
    context={
        'greet':'Welcome',
        'name':'Newsly'

        
        
    }
    request.session['check']=78457894
    print(request.session['check'])
    return render(request,'trail/home.htm',context)
   

        
    }

    return render(request,'trail/home.htm',context)
   
   #  return render(request,'home.html')




class SignUp(View):
    def get(self,request):
        form=UserRegistrationform()
        return render(request,'trail/signup.htm',{'form':form})
    def post(self,request):

        
        form=UserRegistrationform(request.POST)
        
        # request.POST.get('password1','')
        password=request.POST.get('password2','')
        # request.POST.get('email','')
        number=  request.POST.get('phone','')
        
        if form.is_valid():        

          form.save()
                ###### code To Send OTP  generate otp
          rand=random.randint(1000,9999)
          user=User.objects.get(username=request.POST.get('username',''))
          OtpModel(user=user,phone=number,otp=rand,password=password).save()
          print(number)
          request.session['phone']=number
          return HttpResponseRedirect('/verification/')
        else:
          return render(request,'trail/signup.htm',{'form':form})




class Otp(View):
    
    def get(self,request):
        
     
            number=request.session.setdefault('phone','')
            
            form=OtpForm()
        
            return render(request,'trail/otpverification.htm',{'otpform':form,'number':number})
    
        
        
  
    def post(self,request):
        
      try:
          if request.POST.get('send','none')=='Resend':
              rand=random.randint(1000,9999)
              obj=OtpModel.objects.get(phone=request.session['phone'])
              print(f"#############obj.otp############")
      finally:
        
        
        form=OtpForm(request.POST)
        number=request.session['phone']
        
        if form.is_valid():
           
           otp=form.cleaned_data['input1']+form.cleaned_data['input2']+form.cleaned_data['input3']+form.cleaned_data['input4']
           print(f"#######################{otp}")
           tempuser=OtpModel.objects.filter(phone=number).first()
           
           username=tempuser.user.username
           password=tempuser.password
           if otp==tempuser.otp:
              user=authenticate(request,username=username,password=password)
              if user is not None:
               login(request,user)
               return render(request,'trail/home.htm')
           else:
               messages.Warning(request,'Plz enter correct otp')
               return render(request,'trail/otpverification.htm',{'otpform':form,'number':number})
        return render(request,'trail/otpverification.htm',{'otpform':form,'number':number})       


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

