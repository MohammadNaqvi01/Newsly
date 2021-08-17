from django.shortcuts import render,HttpResponse
from .models import Person
# Create your views here



def home(request):
    news=Person.objects.all()
    context={
        'greet':'hello',
        'news':news
    }

    return render(request,'trail/home.html',context)
   
   #  return render(request,'home.html')







