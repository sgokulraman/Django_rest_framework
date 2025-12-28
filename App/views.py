from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo,Task, Ranklist
from .serializers import Task_Serializer, Result_serializer
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
        return Response("Updated Successfully....")
    
    def delete(self, request, Todo_id):
        getting_ids = Todo.objects.get(id = Todo_id)
        getting_ids.delete()
        return Response("Deleted successfully")
    
class Task_seria(APIView):

    def get(self, request, task_id = None):
        if task_id == None:
            all_task = Task.objects.all()
            handle_task = Task_Serializer(all_task, many=True).data
            return Response(handle_task)
        else: 
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
        
    def post(self, request):
        handle_task = Task_Serializer(data = request.data)
        if handle_task.is_valid():
            handle_task.save()
            return Response("Task Added Successfully...")
        else: 
            return Response(handle_task.errors)
    
    def delete(self, request, task_id):
        filter_task = Task.objects.get(id = task_id)
        filter_task.delete()
        return Response( "Deleted successfully...")
        
        
    
class Ranksheet(APIView):
    def post(self, request):
        total_rank = request.data['tamil'] + request.data['english'] + request.data['maths'] + request.data['science'] + request.data['social_science']
        average_rank = total_rank / 5
        if (request.data['tamil']>= 35)and (request.data['english'] >=35) and (request.data['maths'] >=35) and (request.data['science'] >=35) and (request.data['social_science']):
            rank_result = True
            pass
        else:
            rank_result = False
            pass
        
        insert_rank = Ranklist(tamil = request.data['tamil'], english = request.data['english'], maths = request.data['maths'], science = request.data['science'], social_science = request.data['social_science'], total = total_rank, average = average_rank, result = rank_result )
        insert_rank.save()
        # print(insert_rank)
        return Response("Inserted successfully")
    
    def get(self, request, rank_id = None):
        
        if rank_id == None:
            all_rank = Ranklist.objects.all()
            selected = Result_serializer(all_rank, many=True).data
            return Response(selected)
            
        else:
            single_rank = Ranklist.objects.get(id = rank_id)
            selected = Result_serializer(single_rank).data
            return Response(selected)
        #     single_rank = Ranklist.objects.get(id = rank_id)

        #     selected = {
        #         "id" : single_rank.id,
        #         "total": single_rank.total,
        #     }
        # print(selected)
        # return Response(selected)
        
    
    