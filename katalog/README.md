# Penjelasan terkait tugas 2 tentang MVT:

***

1.Kaitan dari views.py, urls.py, models.py, dan berkas html
* Untuk melihat kaitan diantara keempat berkas kita dapat melihat bahwa
views.py akan menerima parameter request yang mana nantinya ia akan mengatur
tampilan pada aplikasi django yang akan di-deploy
* Lalu, urls.py akan berfungsi sebagai pengalih halaman pada web, misalnya
apabila kita menambahkan /katalog/ pada tab search, maka akan diarahkan
ke halaman yang dituju
* Terakhir models.py yang mana berkas ini akan meng-handle permasalahan
tampilan tabel yang akan disinkronisasi dalam berkas html menggunakan
loop for.
* Dengan demikian, berkas html dapat dimasukkan ke dalam django dengan
3 penghubung yaitu views.py, urls.py, dan berkas html

2.Kegunaan Virtual Environment
* Jawaban: virtual environment memberikan ruang yang berisi dependencies
pada masing-masing proyek. Untuk itu, apabila terdapat proyek-proyek
baru yang akan dideploy, maka setiap proyek akan memiliki Virtual
Environment yang berbeda dengan dependencies (package dan lainnya) yang 
berbeda pula. Apabila dalam suatu projek web dibuat tanpa menggunakan 
virtual environment, maka dependencies yang terdapat di dalamnya untuk
menjalankan aplikasi web akan sulit dan tampilannya tidak sesuai ekspektasi

3.Implementasi
* Sesuai dengan step pada lab 1, saya mengimplementasikan deploy ke Heroku
dengan membuat views/tampilan yang dapat menghubungkan berkas html
ke django
* Lalu, routing yang berfungsi sebagai pengalih halaman dan juga models 
juga saya tambahkan pada urls.py dan models.py
* Lalu, saya akan mengetes apakah server dapat dijalankan di localhost
dan tampilan sesuai dengan ekspektasi saya
* Setelah berhasil, maka saya akan membuka heroku dan memasukkan HEROKU_API_KEY
dan HEROKU_APP_NAME di dalam secrets dan dengan adanya procfile
serta dpl.yml, maka akan lebih mudah untuk melihat hasil aplikasinya


___

[LINK](https://radentugas2pbp.herokuapp.com/katalog/) 