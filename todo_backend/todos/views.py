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
    
    elif request.method == 'POST':
        data = request.data
        serializer = TodoSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def todos_detail(request, id):

    try:
        todo = Todo.objects.get(pk=id)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method =='GET':
        serializer = TodoSerializer(todo)

        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method =='PUT':
        data = request.data
        serializer = TodoSerializer(todo, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

    elif request.method == 'PATCH':
        data = request.data
        serializer = TodoSerializer(todo, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method =='DELETE':

        todo.delete()
        return Response({"message": "object succesfully deleted!"}, status=status.HTTP_204_NO_CONTENT)
