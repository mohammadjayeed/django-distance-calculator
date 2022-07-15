from django.urls import path,include
from .views import request_handler_calculate

urlpatterns = [
    
    path('',request_handler_calculate,name="main_app")
]
