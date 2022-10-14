import requests
from urllib import response
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from weather.models import City
from weather.api import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from rest_framework import generics

    
class CityView(generics.ListCreateAPIView):
    serializer_class = serializers.CitySerializer
    
    def get_queryset(self):
        cities = City.objects.all()
        return cities
    
    def get(self, request, *args, **kwargs):
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&APPID=388a86b109f605ab4bf89e8436a5d896"
        weather_data = []
        for city in self.get_queryset():
            response = requests.get(url=url.format(city.name))
            if response.status_code == 200:
                r = response.json()
                weather = {
                    'city': r['name'],
                    'temperature': r['main']['temp'],
                    'description': r['weather'][0]['main'],
                }
                weather_data.append(weather)
                #print(weather)
        serializer = serializers.CityResponseSerializer(weather_data, many=True)
        return Response(data=serializer.data)


    

                  