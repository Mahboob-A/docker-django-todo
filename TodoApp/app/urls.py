
from django.urls import path
from .views import home, update_todo, delete_todo, change_todo_status  #process_from_data

urlpatterns = [
        path('', home, name='home'),
        # path('todo/', process_from_data, name='process_from_data'),
        path('update-todo/<int:todo_id>/', update_todo, name='update_todo'),
        path('delete-todo/<int:todo_id>/', delete_todo, name='delete_todo'),
        path('change-todo-status/<int:todo_id>/<str:status>/', change_todo_status, name='change_todo_status'),
]
