
from django.urls import path
from .views import *

app_name='main_web'

urlpatterns = [
    path('', homepage, name='homepage'),
]
    
