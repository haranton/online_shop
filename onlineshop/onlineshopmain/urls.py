from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('cat/', categories),
    path('about/', about)
]