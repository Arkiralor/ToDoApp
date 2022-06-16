from django.urls import path,include               
from rest_framework import routers                 
from api.api import TodoView                             

router = routers.DefaultRouter()                   
router.register(r'todo', TodoView, 'todo')  

urlpatterns = [
    path('', include(router.urls))             
]