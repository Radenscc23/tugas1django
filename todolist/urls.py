from django.urls import path
from todolist.views import register,login_user,logout_user,show_todolist,new_todo

app_name = 'todolist'

urlpatterns = [
    path('login/', login_user, name='login_user'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout_user'),
    path('', show_todolist, name='show_todolist'),
    path('create/', new_todo, name='new_todo' )
]