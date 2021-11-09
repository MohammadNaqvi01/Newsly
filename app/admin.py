
from django.contrib import admin
from .models import *
# Register your models here.
models_list=[HT,TheHindu,TOI]
@admin.register(*models_list)

class NewslyModelAdmin(admin.ModelAdmin):
     list_display=['id','channel','section','heading','headline','readmore']

@admin.register(OtpModel)
class OtpModelAdmin(admin.ModelAdmin):
    list_display=['id','user','otp','phone','password']

class NewslyAdmin(admin.ModelAdmin):
    pass

class NewslyAdmin(admin.ModelAdmin):
    pass

