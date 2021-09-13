
from django.contrib import admin
from .models import *
# Register your models here.
models_list=[HT,TheHindu,TOI]
@admin.register(*models_list)
class NewslyAdmin(admin.ModelAdmin):
    pass