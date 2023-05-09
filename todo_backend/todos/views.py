from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import *

# Create your views here.

@api_view(['GET', 'POST'])
def todos(request):

    if request.method == 'GET':
        todos = Todo.objects.all()
        serializers = TodoSerializer(todos, many=True)
        return Response(serializers.data, status=200)

