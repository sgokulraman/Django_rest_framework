from rest_framework.routers import DefaultRouter
from .views import Library_view


Library_routers = DefaultRouter()
Library_routers.register(r'details/',Library_view)