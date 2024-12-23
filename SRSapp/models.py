from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=15, default="Jumbi")

    def __str__(self):
        return f"{self.username}"


class Plot(models.Model):
    name = models.CharField(max_length=15) 
    address = models.CharField(max_length=15)  
    price = models.IntegerField()
    location = models.CharField(max_length=10) 
    quality = models.CharField(max_length=20) 
    owner = models.ForeignKey(User, on_delete=models.PROTECT)


    def __str__(self):
        return f"{self.name}"




class Payment(models.Model):
    amount = models.IntegerField()
    date_and_time = models.DateTimeField(auto_now=True)
    plot = models.OneToOneField(Plot, on_delete=models.CASCADE)
    giver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="giver")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")





    def __str__(self):
        return f"{self.plot}"







       