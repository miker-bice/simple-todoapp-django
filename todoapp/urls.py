from django.urls import path
from . import views

urlpatterns = [
    path('', views.todoappView, name='index'),
    path('addTodoItem', views.addTodoView, name='add'),
    path('deleteTodoItem/<int:i>/', views.deleteTodoView, name='delete'),
]
