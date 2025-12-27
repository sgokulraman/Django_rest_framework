from django.urls import path
from .models import Todo
from . import views
urlpatterns = [
    path("api/",views.Todolist.as_view(),name="todolist")
]
