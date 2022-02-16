from .views import RegisterAPI,ClientViewSet,greetings, calculation
from django.urls import path

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/client/',ClientViewSet.as_view({'get': 'list'}),name="client"),
    path('calc', greetings,name="calc"),
    path('calculation/',calculation,name="calculation"),
    # path('calculation/',greetings,name="calculation")
]