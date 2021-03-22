from django.urls import path
from .views import createtodo, updatetodo, deletetodo, signup
app_name = "todo"

urlpatterns = [
    path('', createtodo, name='createtodo'),
    path('signup/', signup, name='signup'),
    path('updatetodo/<str:pk>/', updatetodo, name='updatetodo'),
    path('deletetodo/<str:pk>/', deletetodo, name='deletetodo'),
]
