from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpRequest
from todolist.models import Task
from django.contrib.auth.decorators import login_required
from django import forms

# Create your views here.
class CreateNewForm(forms.Form):
    date = forms.DateField(label="Tanggal")
    title = forms.CharField(label="Judul")
    description = forms.CharField(label="Deskripsi", widget=forms.Textarea)

@login_required(login_url='/todolist/login/')
def show_todolist(request: HttpRequest):
    todolist = Task.objects.all().filter(user = request.user)
    context = {"todolist":todolist}
    return render(request, "list_of_todo.html", context)

def new_todo(request: HttpRequest):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        Task.objects.create(
            user= request.user,
            title = title,
            description = description,
        )
        return HttpResponseRedirect(reverse("todolist:show_todolist"))
    return render (request, "todolist_create.html")

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login_user')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    return render(request, 'login.html')

def logout_user(request: HttpRequest):
    logout(request)
    return redirect('todolist:login_user')

@login_required(login_url='/todolist/login/')
def perubahan_status(request, id):
    getstatus = Task.objects.get(pk = id)
    if getstatus.is_finished:
        getstatus.is_finished = False
    else:
        getstatus.is_finished = True
    getstatus.save()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))

@login_required(login_url='/todolist/login/')
def delete_list(request,id):
    deletelist = Task.objects.get(pk = id)
    deletelist.delete()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))



    
    