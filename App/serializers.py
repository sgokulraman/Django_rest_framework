from rest_framework.serializers import ModelSerializer
from . import models

class Task_Serializer(ModelSerializer):
    class Meta:
        
        model = models.Task
        fields = "__all__"