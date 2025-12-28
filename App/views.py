from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo,Task
from .serializers import Task_Serializer
class TodoList(APIView):
    def get(self, request):
        print(request)
        geting_object = Todo.objects.all()
        todo_list = []
        for s in geting_object:
            object_dir = {
                "id" : s.id,
                "title" : s.title,
                "date" : s.date,
                "time" : s.time
            }
            todo_list.append(object_dir)
            
        return Response(todo_list)
    
    
    def post(self, request):
        print(request.data)
        selected_item = Todo(title = request.data['title'])
        selected_item.save()
        return Response("Your request successfully accepted")
    
class updatedeletetodo(APIView):      

    def patch(self, request, Todo_id):
        getting_ids = Todo.objects.filter(id = Todo_id)
        getting_ids.update(title = request.data["title"])
        return Response(f"Updated Successfully....{request.data}")
    
    def delete(self, request, Todo_id):
        getting_ids = Todo.objects.get(id = Todo_id)
        getting_ids.delete()
        return Response("Deleted successfully")
    
class Task_seria(APIView):
    def post(self, request):
        handle_task = Task_Serializer(data = request.data)
        if handle_task.is_valid():
            handle_task.save()
            return Response("Task Added Successfully...")
        else: 
            return Response(handle_task.errors)
        
        
    def get(self, request):
        all_task = Task.objects.all()
        handle_task = Task_Serializer(all_task, many=True).data
        return Response(handle_task)
    
class TaskViewById(APIView):  
    def get(self, request, task_id):
        task = Task.objects.get(id = task_id)
        handle_task = Task_Serializer(task).data
        return Response(handle_task)
    
    def patch(self, request,task_id):
        task = Task.objects.get(id=task_id)
        update_task = Task_Serializer(task, data= request.data, partial=True)# This partial can't be generate error
        if update_task.is_valid():
            update_task.save()
            return Response("Updated Successfully")
        else:
            return Response(update_task.errors)
        
        
    def put(self, request, task_id):
        task = Task.objects.get(id=task_id)
        update_task = Task_Serializer(task, data= request.data, partial=True)# This partial can't be generate error
        if update_task.is_valid():
            update_task.save()
            return Response("Updated Successfully")
        else:
            return Response(update_task.errors)