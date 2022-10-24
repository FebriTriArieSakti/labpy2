# Belajar Bahasa Pemograman Python
Pertama kita harus mendownload dulu program [Python 3.10](https://www.python.org/).

# Buka Program Python dengan CMD Path
Buka Command Prompt di PC kalian.

![gambar1](gambar/cmd4.jpg)

Kemudian panggil path Python dengan  command ***python***.
> python

![gambar2](gambar/cmd1.jpg)

# Masukkan Perintah Dasar Python
Menampilkan Tulisan dengan perintah ***print***.
> print("Hello")
>
> print("Saya sedang belajar Python")

![gambar2](gambar/cmd2.jpg)

# Menjumlahkan 2 Bilangan Menggunakan Variable
- Mendefinisikan variable ***a*** dengan nilai 8
- Mendefinisikan variable ***b*** dengan nilai 6
- Mencetak nilai variable ***a*** dan ***b***
- Mencetak hasil penjumlahan ***a + b***

> ***a*** = 8
> 
> ***b*** = 6
> 
> print ("variable a=",***a***)
> 
> print ("variable b=",***b***)
> 
> print ("hasil penjumlahan a+b",***a+b***)

![gambar2](gambar/cmd3.jpg)

# Belajar Program Idle (Python)
Buka program Idle dan kita coba untuk Menentukan Hasil Penggabungan, Penjumlahan, dan Pembagian.
### Menggunakan fungsi ***Input*** untuk mengambil nilai variabel dari keyboard
> ***input nilai variable***
> 
> a=input("Masukkan nilai a:")
> 
> b=input("Masukkan nilai b:")
>
> ***cetak nilai variable***
> 
> print("Variabel a=",a)
> 
> print("Variabel b=",b)
> 
> ***cetak hasil operasi kedua dengan String Format***
> 
> print("Hasil penggabungan {1}&{0}=%s".format(a,b) %(a+b))
>
> ***konversi nilai variable***
> 
> a=int(a)
> 
> b=int(b)
> 
> print("Hasil penjumlahan {1}+{0}=%s".format(a,b) %(a+b))
> 
> print("Hasil pembagian {1}/{0}=%s").format(a,b) %(a/b))

![gambar1](gambar/idle1.jpg)

Jika sudah kita coba untuk Run program yang telah kita buat!

![gambar1](gambar/idle3.jpg)

> ⚠ Pastikan lokasi penyimpanannya di dalam Folder: **labpy2/**.

![gambar1](gambar/idle2.jpg)

# Pycharm

<p align="left">
  <a href="https://www.jetbrains.com/pycharm/download/">
      <img width="200" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/PyCharm_Icon.svg/2048px-PyCharm_Icon.svg.png">
  </a>
</p>

Setelah semua selesai, kita lanjut belajar program [PyCharm](https://www.jetbrains.com/pycharm/download/) 

##Buka Program PyCharm
Buat Project Baru/ New Project, dan pastikan lokasi project berada di dalam Folder: **labpy2/**.

![gambar1](gambar/pycharm1.jpg)

Buat File Python baru,

![gambar1](gambar/pycharm2.jpg)

dan beri nama "main"

![gambar1](gambar/pycharm3.jpg)

Kemudian kita masukan perintah untuk menghitung Luas dan Keliling Lingkaran
> r = input("Masukkan jari-jari lingkaran : ")
> 
> pi = 3.14
> 
> l = pi * int(r) * int(r)
> 
> k = 2 * pi * int(r)
> 
> print("Luas Lingkaran     : ",l)
> 
> print("Keliling Lingkaran : ",k)

![gambar1](gambar/pycharm4.jpg)


