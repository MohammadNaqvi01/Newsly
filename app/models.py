from django.db import models

from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.db.models.fields.related import OneToOneField


class Newsly(models.Model):
      section=models.CharField(max_length=255)
      heading = models.CharField(max_length=255)
      headline= models.CharField(max_length=500)
      readmore= models.CharField(max_length=500)
      

      class Meta:
       abstract = True
       

class TheHindu(Newsly):
    channel=models.CharField(max_length=100,default="TheHindu")
    
    def __str__(self):
        return str(self.id)
    
    class Meta():
       #verbose_name
       db_table='newslyth'
       constraints=[
           models.UniqueConstraint(fields=['section','heading','headline','readmore'],name="TH")
       ]
      
class TOI(Newsly):
    channel=models.CharField(max_length=100,default="TOI")
    
    def __str__(self):
        return str(self.id)
    
    class Meta():
       db_table='newslytoi'
       constraints=[
           models.UniqueConstraint(fields=['section','heading','headline','readmore'],name="TOI")
       ]
class HT(Newsly):
     channel=models.CharField(max_length=100,default="HT")
    
     def __str__(self):
        return str(self.id)
    
     class Meta():
       db_table='newslyht'
       constraints=[
           models.UniqueConstraint(fields=['section','heading','headline','readmore'],name="HT")
       ]

#Extending user model using One to One field
class OtpModel(models.Model):
   user=OneToOneField(User,on_delete=models.CASCADE)
   otp=CharField(max_length=4)
   phone=CharField(max_length=13)
   password=CharField(max_length=20,default='')
    #  class Meta():
    #    constraints=[
    #        models.UniqueConstraint(fields=['text'],name="text")
    #    ]

   def __str__(self):
        return str(self.id)

