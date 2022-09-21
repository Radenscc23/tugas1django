### Pertanyaan dan jawaban dalam README.md

1.Jelaskan perbedaan antara JSON, XML, dan HTML!
* JSON = Pada dasarnya JSON atau `JavaScript Object Notation` adalah sebuah format penyimpanan data dan bersifat indenpenden karena format ini dapat digunakan di berbagai bahasa pemrograman. Dikarenakan merupakan sebuah turunan dari bahasa pemrograman Javascript, format JSON otomatis terdesain sebagai sebuah format *self-describing* yang menyebabkan JSON menjadi lebih mudah untuk dimengerti. Pada umumnya, JSON akan menampilkan data yang tersimpan pada sebuah program dalam bentuk *text*.

* XML = XML atau `eXtensible Markup Language` adalah format kedua untuk membawa dan bukan menyimpan suatu data dalam program baik aplikasi *mobile* maupun *web*. Tujuan utama pada XML berfokus pada kesederhanaan, *usability*, dan juga *generality* kepada seluruh *programmer* yang ingin mengaplikasikan XML dalam membawa data. Berbeda dengan JSON, XML bersifat *self-descriptive* yang artinya kita sebagai *user* dapat mengerti mengenai data apa yang disampaikan. 

* HTML = HTML merupakan sebuah bahasa standar pemrograman yang dibuat sebagai pengisi halaman depan pada sebuah website. Berbeda dengan XML ataupun JSON yang mana keduanya berhubungan dalam membawa maupun menyimpan sebuah data, HTML berfungsi sebagai penampil dari data tersebut. Umumnya, HTML sendiri akan berperan sebagai sebuah `bahasa desain` untuk menentukan letak-letak bagian *header*, *subheader*, *footer*, maupun bagian lainnya untuk mempercantik bagian dasar pada *website*.

2.Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
* Jawaban = *data delivery* merupakan sebuah langkah terpenting dalam sebuah pengembangan platform untuk mendistribusikan data dari satu *stack* ke dalam *stack* lainnya. Dengan adanya distribusi data ini, maka fungsionalitas platform (dalam *web* maupun *mobile*)akan lebih mudah digunakan oleh seorang user baik dari visualisasi maupun sisi teknis. 

3.Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
* Langkah pertama yang saya lakukan yaitu membuat aplikasi mywatchlist di dalam *clone repository* dengan command python yaitu `python manage.py startapp mywatchlist`

* Langkah kedua dimulai setelah saya membuat aplikasi. Saya beranjak ke dalam models.py dengan menambah potongan kode berikut: 

```
class filmWatchlist(models.Model):
    watchedmovies = models.BooleanField(max_length=50)
    titlemovie = models.TextField()
    ratingmovie = models.IntegerField()
    moviereleasedate = models.TextField()
    reviewmovie = models.TextField()
```
* Namun, sebelum saya melanjutkan pengisian kode, saya melakukan migrasi untuk mempersiapkan migrasi model ke *database* Django dengan *command* `python manage.py makemigrations` dan dilanjutkan dengan `python manage.py migrate`

* Setelah itu, saya membuat sebuah file dengan format JSON sebagai penyimpan data dalam tampilan *template* Django dengan nama `initial_mywatchlist_data.json`. 

* Untuk memasukkan format JSON ke dalam *database* setelah menambahkan beberapa film dan data nya melalui suatu situs, saya melakukan *command* `python manage.py loaddata initial_mywatchlist_data.json`.

* Langkah selanjutnya dimulai dengan implementasi *views* dasar dengan memodifikasi data di views.py, kedua urls.py dalam mywatchlist dan project_django, lalu juga pada file html

* Setelah melakukan implementasi dasar, maka saya menghubungi *views* dan *template* dengan menambahkan beberapa fitur dalam views.py dan html

* Lalu, *save semua file dan jalankan di localhost dengan command `python manage.py runserver` untuk melihat hasilnya.

* Agar dapat diimplementasi dalam bentuk XML, kita perlu menambah beberapa *lines of code* dalam views.py diantaranya

```
def show_in_xml(request):
    data = filmWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

dengan menambahkan import 

```
from django.http import HttpResponse
from django.core import serializers
```

lalu dilanjutkan dengan baris kode `path('xml/', show_in_xml, name='show_in_xml'),` di dalam urls.py dalam folder mywatchlist

* Agar dapat diimplementasi dalam bentuk JSON, kita perlu menambah beberapa *lines of code* dalam views.py diantaranya

```
def show_movie_in_json(request):
    data = filmWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

dan dilanjutkan dalam urls.py dalam folder mywatchlist yaitu `path('json/', show_movie_in_json, name='show_movie_in_json'),`

* Setelah selesai, maka kita dapat mengetesnya dalam localhost dengan command `python manage.py runserver`

---
### Finally, My Links: 
- [HTML](https://radentugas2pbp.herokuapp.com/mywatchlist/html/)
- [XML](https://radentugas2pbp.herokuapp.com/mywatchlist/xml/)
- [JSON](https://radentugas2pbp.herokuapp.com/mywatchlist/json/)


