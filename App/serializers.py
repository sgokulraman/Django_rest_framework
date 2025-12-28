from rest_framework.serializers import ModelSerializer
from . import models

class Task_Serializer(ModelSerializer):
    class Meta:
        
        model = models.Task
        fields = "__all__"
        
class Result_serializer(ModelSerializer):
    class Meta:
        model = models.Ranklist
        
        fields = "__all__"