from django.urls import path, include
from .router import Library_routers
urlpatterns = [
    path("books/",include(Library_routers.urls)),
]
