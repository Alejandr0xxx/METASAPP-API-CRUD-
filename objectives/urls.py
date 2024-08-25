from django.urls import path
from .views import *
urlpatterns = [
    path('', home),
    path('api/', objectives_path),
    path('api/<int:pk>/', objective_path)
]