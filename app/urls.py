
from django.urls import path
from app import views
urlpatterns = [

    path('',views.home,name="home"),

   
    path('signup/',views.SignUp.as_view(),name="signup"),

    path('verification/',views.Otp.as_view(),name="login"),
    path('check/',views.check),
    

    path('login/',views.Otp.as_view(),name="login"),

    path('login/',views.Otp.as_view(),name="login"),

]
