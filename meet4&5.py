# Inputan dari user
# Aritmatika

# Belajar Inputan
Bima = input("Masukan Kata : ")
print("isi dari Bima :", Bima, "bertipe data :", type(Bima))

# Belajar aritmatika dasar
x = 9
y = 4

# Contoh penjumlahan +
hasil = x + y
print ("x + y =", hasil)

# Pengurangan -
hasil = x - y
print ("x - y =", hasil)

# Perkalian *
hasil = x * y
print ("x * y =", hasil)

# Pembagian /
hasil = x / y
print ("x / y =", hasil)

# Perpangkatan exponen **
hasil = x ** y
print ("x ^ y =", hasil)

# Modulus %
hasil = y % x
print ("x mod y =", hasil)

# Floor division (pembulatan kebawah) //
hasil = x // y
print (" x // y =", hasil)

# Aritmatika prioritas
# () , exponen, perkalian/pembagian, penjumlahan/pengurangan
x = 3
y = 4
z = 5

hasil = (x ** y * (z + x) / y - z % x // y)
print ("x ** y * (z + x) / y - z % x // y = ",hasil)