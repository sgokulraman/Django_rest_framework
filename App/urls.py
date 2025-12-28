from django.urls import path
from . import views
urlpatterns = [
    path("api/",views.TodoList.as_view(),name="todolist"),
    path("api/<int:Todo_id>/", views.TodoList.as_view(),name="todolistid"),
    path('task/',views.Task_seria.as_view(),name="task"),
    path('task/<int:task_id>/',views.Task_seria.as_view(),name='taskbyid'),
    path('ranklist/',views.Ranksheet.as_view()),
    path('ranklist/<int:rank_id>/', views.Ranksheet.as_view()),
]
