from django.urls import path
from weather.api.views import CityView

urlpatterns = [
    path('', CityView.as_view())
]