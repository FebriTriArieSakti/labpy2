# input nilai variable

a=input("Masukkan nilai a:")

b=input("Masukkan nilai b:")

# cetak nilai variable

print("Variabel a=",a)

print("Variabel b=",b)

# cetak hasil operasi kedua dengan String Format

print("Hasil penggabungan {1}&{0}=%s".format(a,b) %(a+b))

# konversi nilai variable

a=int(a)

b=int(b)

print("Hasil penjumlahan {1}+{0}=%s".format(a,b) %(a+b))

print("Hasil pembagian {1}/{0}=%s".format(a,b) %(a/b))
