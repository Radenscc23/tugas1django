from django.urls import path
from todolist.views import register,login_user,logout_user,show_todolist,new_todo,perubahan_status,delete_list,show_in_json,add_json,delete_json

app_name = 'todolist'

urlpatterns = [
    path('login/', login_user, name='login_user'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout_user'),
    path('', show_todolist, name='show_todolist'),
    path('create/', new_todo, name='new_todo' ),
    path('perubahan_status/<int:id>/', perubahan_status, name='perubahan_status'),
    path('delete_list/<int:id>/', delete_list, name='delete_list'),
    path('json/', show_in_json, name='show_in_json'),
    path('add/', add_json, name='add_json'),
    path('delete/<int:id>/', delete_json, name = 'delete_json')
]