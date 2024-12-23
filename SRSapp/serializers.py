from . models import *
from rest_framework import serializers




class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = "__all__"




class PlotSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Plot
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Payment
        fields = "__all__"



    

