# Program Menentukan Bilangan Terbesar dari 3 Bilangan

# Memasukkan tiga bilangan
a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))

# Menentukan bilangan terbesar
if a > b and a > c:
    terbesar = a
elif b > a and b > c:
    terbesar = b
else:
    terbesar = c

# Menampilkan hasil
print("Bilangan terbesar adalah:", terbesar)
