
from django.urls import path
from app import views
urlpatterns = [

    path('',views.home,name="home"),

   
    path('signup/',views.SignUp.as_view(),name="signup"),
    path('login/',views.Otp.as_view(),name="login"),
    
]
