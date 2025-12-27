from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Todo
class Todolist(APIView):
    def post(self, request):
        print(request.data)
        fetching_data = Todo(title = request.data["title"])
        fetching_data.save()
        return Response("Successfully Created New Todo List")