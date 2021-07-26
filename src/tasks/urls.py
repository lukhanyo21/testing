from django.urls import path
from .views import tasks, edit_task, task_delete

app_name = "tasks"
urlpatterns = [

    path('', tasks, name='tasks'),
    path('add/', edit_task, name='add_task'),
    path('edit/<id>', edit_task, name="edit_task"),
    path('delete/<id>', task_delete, name="delete_task"),

]
