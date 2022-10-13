### Tugas 6 PBP
1.Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
* Asynchronous programming adalah suatu teknik programming yang mana memiliki sifat multi-thread. Berarti bahwa Asynchronous dapat menjalankan beberapa operasi tanpa harus menjalankannya satu persatu. Berbeda dengan synchronous yang harus menjalanka secara satu persatu

2.Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
* Paradigma event-driven programming ditentukan oleh tindakan user ketika menjalankan program django. Kita bisa lihat contoh event-driven programming seperti onClick ataupun onReady

3.Jelaskan penerapan asynchronous programming pada AJAX.
* Penerapan asynchronous programming pada AJAX dapat diimplementasikan melalui back thread. Dengan adanya proses ini, maka runtime akan dieksekusi oleh compiler tanpa ada kendala saat menambahkan kode

4.Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
* Menambahkan fungsi baru untuk menampilkan data dalam JSON pada `views.py`
* Menambahkan path-path baru berdasarkan nama fungsi yang sudah dibuat
* Menambahkan script pada `list_of_todo.html` sehingga kita dapat melihat perubahannya
* Menambahkan tombol dengan modal dan di hook dengan onClick