from rest_framework import serializers
from dataclasses import field

from weather.models import City

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"
        

class CityResponseSerializer(serializers.Serializer):
    city = serializers.CharField(required=True, allow_blank=False, max_length=150)
    description = serializers.CharField(required=True, allow_blank=False, max_length=250)
    temperature = serializers.FloatField()
    
 
