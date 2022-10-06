### TUGAS 4 PBP

1.Kegunaan {% csrf_token %} pada elemen `<form>`
* CSRF atau *Cross Side Request Forgery* adalah suatu *built in* yang terdapat pada *framework* Django yang memiliki fungsi untuk melindungi website dari serangan-serangan berbahaya para peretas. {% csrf_token %} akan menghasilkan sebuah token yang dapat digunakan saat merender halaman website. Dengan demikian, *user* yang memiliki token ini akan diautentikasi oleh website agar dapat terdaftar dalam database

* Apabila {% csrf_token %} tidak terdapat pada `<form>`, maka terdapat kemungkinan besar bagi para peretas untuk melakukan serangan-serangan berupa virus ataupun malware ke dalam website yang akan dibuat

2.Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.

* Tentu saja bisa, secara garis besar, elemen `<form>` pada HTML dapat dibuat secara manual apabila kita menggunakan potongan kode berikut

```
<table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
```
* Dengan contoh pada potongan kode diatas, secara garis besar kita dapat menggunakan elemen `<td>` untuk menggantikan {{ form.as_table }}) secara manual.

3.Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
* Untuk menyimpan data pada database Django lokal, terdapat suatu command yang bernama `python manage.py makemigrations` dan `python manage.py migrate`. 
* Pertama `python manage.py makemigrations` berfungsi untuk mempersiapkan migrasi di dalam `models.py` agar models yang dibuat dapat masuk ke database lokal Django
* Setelah itu command `python manage.py migrate` akan menjadi command yang berfungsi untuk mengantar models untuk masuk ke dalam database django lokal
* Dengan demikian data pada `models.py` aan tersimpan pada template HTML 

4.Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
* Pertama, saya buat `models.py` terlebih dahulu untuk mengimplementasikan tampilan awal yang akan dimasukkan ke dalam Database Django lokal
* Lalu, dengan command `python manage.py makemigrations` dan `python manage.py migrate`, maka models yang terdapat pada `models.py` akan terbentuk dan masuk ke dalam database
* Setelah itu, kita dapat mengimplementasikan `views.py` untuk menyiapkan tampilan dan rendering untuk menyambungkan satu page ke page yang lain

```
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
        getstatus.is_finised = True
    getstatus.save()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))

@login_required(login_url='/todolist/login/')
def delete_list(request,id):
    deletelist = Task.objects.get(pk = id)
    deletelist.delete()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))
```

* Setelah kita selesai dengan views.py maka kita dapat melakukan routing di dalam `urls.py` 

```
from django.urls import path
from todolist.views import register,login_user,logout_user,show_todolist,new_todo,perubahan_status,delete_list

app_name = 'todolist'

urlpatterns = [
    path('login/', login_user, name='login_user'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout_user'),
    path('', show_todolist, name='show_todolist'),
    path('create/', new_todo, name='new_todo' ),
    path('perubahan_status/<int:id>/', perubahan_status, name='perubahan_status'),
    path('delete_list/<int:id>/', delete_list, name='delete_list'),
]
```

* Lalu, kita dapat membuat tampilan dasar pada setiap file HTML yang dimulai dari `login.html`
```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul >
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Belum mempunyai akun? <a href="{% url 'todolist:register' %}">Buat Akun</a>

</div>

{% endblock content %}
```

* `register.html`

```
{% extends 'base.html' %}

{% block meta %}
<title>Registrasi Akun</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Formulir Registrasi</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```
* `list_of_todo.html`
```
{% extends 'base.html' %}

{% block meta %}
<title>List of Todo's</title>
{% endblock meta %}

{% block content %}

<p>Selamat datang {{user.get_username}} | <a href= "{% url 'todolist:logout_user' %}">Log out</a></p>
<a href = "{% url 'todolist:new_todo' %}"> Tambah List</a>

<table border = "4">
    <tr>
      <th>Date</th>
      <th>Title</th>
      <th>Description</th>
    </tr>
    {% for todo in todolist %}
      <tr>
          <th>{{todo.date}}</th>
          <th>{{todo.title}}</th>
          <th>{{todo.description}}</th>
          {% if getstatus.isfinished %}
            <th> Selesai </th>
          {% else %}
            <th> Belum Selesai </th>
          {% endif %}

          <th><button><a href = "{%url 'todolist:perubahan_status' todo.id %}">Cek Status</a></button></th>
          <th><button><a href = "{%url 'todolist:delete_list' todo.id %}">Delete</a></button></th>

      </tr>
    {% endfor %}
  </table>

 {% endblock content %}
 ```

 * dan yang terakhir `todolist_create.html`
 ```
 {% extends 'base.html' %}

{% block meta %}
<title>Tambah Todo</title>
{% endblock meta %}

{% block content %}
<div class = "login">

    <h1>Tambah Todo</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                <tr>
                <td>Title:</td>
                <td><input type= "text" name= "title" placeholder="Title"></td> 
                </tr>
                <tr>
                    <td>Description:</td>
                    <td><input type= "text" name= "description" placeholder="Description"></td> 
                    </tr>
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Buat" href="{%url 'todolist:show_todolist' %}"/></td>  
                </tr>  
            </table>  
        </form>
    {% if messages %}  
        <ul >   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>

{% endblock content %}
```

* Namun, jangan lupa untuk menambahkan routing pada `views.py` yang terletak pada file project_django
* Setelah saya selelsai dengan seluruh code diatas, maka saya deploy ke aplikasi heroku

### Tambahan pertanyaan pada tugas 5 PBP
1.Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
* Inline merupakan sebuah properti CSS yang nantinya akan dipakai pada *attachment* pada berkas HTML. Pada dasarnya kelebhannya adalah kita dapat mengimplementasikannya langsung tanpa harus membuat `<style>` di luar div yang diinginakan. Sayangnya, Inline tidak dapat diimplementasikan dengan CSS murni
* Internal merupakan properti CSS yang berada di dalam file HTML yang nantinya akan dimasukkan ke dalam tag `<style>`. Kelebihannya terdapat pada efektivitas codingan karena tidak memerlukan file baru, tetapi akan terlihat tidak rapi apabila digabungkan dalam satu file
* External merupakan properti CSS yang berada dalam file diluar file HTML yang nantinya akan dihubungan melalui static.css. Kelebihannya yaitu file akan terlihat lebih rapi karena berada di luar HTML, namun tidak seefektif Internal yang mana kita dapat melihat setiap tag HTML tanpa harus melihat file berbeda lagi

2.Jelaskan tag HTML5 yang kamu ketahui.
* `<link>` -> tag yang menghubungkan antar satu page ke page lainnya
*  `<table>` -> tag yang membuat suatu tabel dengan deskripsi-deskripsinya
* `<button>` -> tag yang akan membuat suatu tombol yang akan melakukan beberapa action (misalnya logout)

3.Jelaskan tipe-tipe CSS selector yang kamu ketahui.
* `*` -> memilih semua elemen yang termasuk di dalam HTML
* `.class` -> memilih semua elemen yang termasuk di dalam class HTML (misalnya .intro)

4.Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
* Pertama-tama saya menambahkan bootstrap pada setiap page HTML dengan
```
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
```

* Setelah itu di dalam file selain list_of_todo.html saya menambah beberapa fitur seperti button dan fitur-fitur bootstrap lainnya, contoh

* login.html
```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
  </head>
<style>

    body{
        background-color:#4f427e
    }
    table{

        margin: auto;
        font-size: 20px;
        font-family: sans-serif;
        font-weight: bold;
        color: #25e6d6;
    }
    
    
</style>
<body>
<div class = "login">

    <h1 class = "text-4xl font-bold text-center">Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <div class="d-grid gap-2 d-md-block">
                <td></td>
                <td><input class="btn btn-primary" type="submit" value="Login"></td>
            </div>
            </tr>
            
        </table>
    </form>

    {% if messages %}
        <ul >
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    <h5>Belum mempunyai akun? </h5>
    <a class = "btn btn-secondary" href="{% url 'todolist:register' %}">Buat Akun</a>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
</div>
</body>

{% endblock content %}
```

* register.html
```
{% extends 'base.html' %}

{% block meta %}
<title>Registrasi Akun</title>
{% endblock meta %}

{% block content %}  
<head>

    
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
  </head>

  <style>
     body{
        background-color:#4f427e
    }
    table{
        font-size: 20px;
        font-family: sans-serif;
        color: #25e6d6;
    }
  </style>
<div class = "login">
    
    <h1>Formulir Registrasi</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input class = "btn btn-primary" type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
</div>  

{% endblock content %}
```
* todolist_create
```
{% extends 'base.html' %}

{% block meta %}
<title>Tambah Todo</title>
{% endblock meta %}

{% block content %}

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
  </head>

<style>

    body{
        background-color:#4f427e
    }
    table{

        margin: auto;
        font-size: 20px;
        font-family: sans-serif;
        font-weight: bold;
        color: #25e6d6;
    }
    
    
</style>
<body>
<div class = "login">

    <h1 class = "text-4xl font-bold text-center">Tambah Todo</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                <tr>
                <td>Title:</td>
                <td><input type= "text" name= "title" placeholder="Title"></td> 
                </tr>
                <tr>
                    <td>Description:</td>
                    <td><input type= "text" name= "description" placeholder="Description"></td> 
                    </tr>
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Buat" href="{%url 'todolist:show_todolist' %}"/></td>  
                </tr>  
            </table>  
        </form>
    {% if messages %}  
        <ul >   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
</div>
</body>
{% endblock content %}

```

* Untuk menambah card pada tampilan todo, maka saya menambahkan atribut card bootstrap

```
{% extends 'base.html' %}

{% block meta %}
<title>List of Todo's</title>
{% endblock meta %}

{% block content %}
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">


<h2 class = "text-4xl font-bold text-center">Selamat datang {{user.get_username}} | <a href= "{% url 'todolist:logout_user' %}">Log out</a></h2>
<h2 class = "text-4xl font-bold text-center"><a href = "{% url 'todolist:new_todo' %}"> Tambah List</a></h2>

  <div class ="card-group">
    {% for todo in todolist %}
      <div class="card border-primary mb-3" style="max-width: 18rem;">
        <div class="card-body">
          <div class="card-action"></div>
          <h1 class = "card-title">{{todo.title}}</h1>
          <p class = "card-text">{{todo.description}}</p>
          <p class = "card-text">{{todo.date}}</p>
          <p>{{todo.is_finished|yesno:"Selesai,Belum Selesai"}}</p>
          
          <form action = "{%url 'todolist:perubahan_status' todo.id %}" method = "POST">
            {% csrf_token %}
            <button class = "btn btn-light">Cek Status</button>
          </form>
         
          <form action = "{%url 'todolist:delete_list' todo.id %}" method = "POST">
            {% csrf_token %}
          <button class="btn btn-light">Delete</button>
        </form>
        </div>
      </div>
     
    {% endfor %}
  </div> 


 {% endblock content %}
 ```

# THE LINK IS BELOW
1. [Todolist App](https://radentugas2pbp.herokuapp.com/todolist/login/?next=/todolist/)