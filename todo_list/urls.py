
from django.contrib import admin
from django.urls import path,include
from todo import views

urlpatterns = [
     path('admin/', admin.site.urls),
     path('todo_list/', views.todo_list, name='todo_list'),  
      path('complete_todo/<int:todo_id>/', views.complete_todo, name='complete_todo'),
]