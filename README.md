# Lab-6
Repository ini dibuat untuk memenuhi tugas di pertemuan-10 <br>
<pre>
Nama    : Naufal Nirwansyah 
Kelas   : TI.20.A1
NIM     : 312010174
Dosen   : Agung Nugroho S.Kom, M.Kom
</pre>
***

**Berikut ini tugas yang diberikan oleh dosen saya :** <br>

<div align="center">
<img src="images/lab6task.png" >
</div> <br>

Untuk membuat task diatas saya dengan source code sebagai berikut: <br>
**Data** & **Main Script**
<br>
<br>
**Untuk membuat file **Data** tersebut saya menggunakan source code dibawah ini :** <br>

<div align="center">
<img src="images/booksc.png" >
</div> <br>

Kemudian kita *save* di folder sendiri, disini saya menyimpan file **Data** kedalam folder **Data** dan saya simpan dengan file name *book*. <br>

<div align="center">
<img src="images/data1.png" >
</div> <br>

Source Code diatas berfungi sebagai berbagai *action syntax* yang nanti akan di run di file **Main Script**.
<br>
**Kemudian untuk file **Main Script** nya sendiri saya menggunakan source code sebagai berikut :**

<div align="center">
<img src="images/main.png" >
</div> <br>


**Kemudian setelah 2 file tersebut dibuat, lalu kita run. Maka akan menghasilkan output sebagai berikut:**
<div align="center">
<img src="images/result.png" >
</div> <br>

**Dan disitu kita punya 6 opsi:** <br>

**Lihat** <br>
**Tambah** <br>
**Hapus** <br>
**Ubah** <br>
**Cari** <br>
**Keluar** <br>

Mari kita coba opsi T (Tambah) dari source code **Book** diatas, maka output yang keluar adalah sebagai berikut : <br>

<div align="center">
<img src="images/tambah.png" >
</div> <br>

Berjalan sesuai dengan yang kita inginkan. <br>
<br>

**Sekarang kita akan mencoba opsi **Ubah**:** <br>

<div align="center">
<img src="images/ubah.png" >
</div> <br>

Data **Kelas** dari table sebelumnya berhasil kita ubah dengan opsi **Ubah**, Selanjutkan kita akan mencoba opsi **Hapus** : <br>
Berikut tampilan dari menu **Hapus** : <br>

<div align="center">
<img src="images/hapus.png" >
</div> <br>
<br>

Untuk opsi **Lihat** dan **Keluar** dua opsi tersebut akan menampilkan result table yang sudah kita isi dengan data, setelah melalui proses sebelumnya.

***
## Penjelasan

- `from data import book` = Syntax ini berfungsi untung *menginport* file *book* dari folder data.

- `data={}` : Ini digunakan untuk menampung list dengan format **dictionary**. <br>

- `menu = input("(L) Lihat, (T) Tambah, (H) Hapus, (U) Ubah, (C) Cari, (K) Keluar: ")` : Untuk menambah opsi **Tambah/Ubah/Hapus/Lihat/Cari/Keluar** dari variable menu. <br>

- `break` : untuk menghentikan seluruh proses yang berjalan. <br>

- `book.add()` : untuk summon dan run perintah dari sumber `book`

- `book.show()` : untuk menampilkan sub menu `show` dari sumber `book` <br>

- `sub_data = input("(Semua), (Nama), (NIM), (Kelas), (NoTelepon), (AsalKota): ")` Untuk menambah pilihan opsi **Nama/NIM/Kelas/No Telepon/Asal Kota** dari variable opsi **Ubah**. <br>

***
## Flowchart
<div align="center">
<img src="images/flowchart.png" >
</div> <br>


***
**Sekian tugas saya untuk Repository ini, Terimakasih.**
<br>

![ttd](images/tttd.png)
<br>

**Naufal Nirwansyah**
