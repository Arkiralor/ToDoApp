from .serializers import TodoSerializer 
from rest_framework import viewsets      
from api.models import Todo
from api.serializers import TodoSerializer            

class TodoView(viewsets.ModelViewSet):  
    serializer_class = TodoSerializer   
    queryset = Todo.objects.all() 