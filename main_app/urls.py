from django.urls import path
from numpy import delete
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/delete_todo', views.DeleteTodo.as_view(), name='delete_todo')
]