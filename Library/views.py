from rest_framework.viewsets import ModelViewSet
from .models import Books
from .serializers import Library_Serializers

class Library_view(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = Library_Serializers
    