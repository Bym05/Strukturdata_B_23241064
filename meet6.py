# Perbandingan
# lebih besar >
# lebih kecil <
# lebih besar >=
# lebih kecil <=
# sama dengan ==
# tidak sama dengan !=
# sama "is"
# tidak sama "is not"

x = 4
y = 5

# Lebih Dari
hasil = x > y
print(x, '>', y, 'adalah', hasil)

# Kurang dari
hasil = x < y
print(x, '<', y, 'adalah', hasil)

# Lebih dari sama dengan >=
hasil = x >= 2
print(x, '>=', 2, 'adalah', hasil)
print(x, '>=', 4, 'adalah', hasil)

# Kurang dari sama dengan <=
hasil = x <= 2
print(x, '<=', 2, 'adalah', hasil)
hasil = x <= 4
print(x, '<=', 4, 'adalah', hasil)
hasil = x <= y
print(x, '<=', y, 'adalah', hasil)

# Sama dengan ==
hasil = x == y
print(x, '==', y, 'adalah', hasil)

# Tidak sama dengan !=
hasil = x != y
print(x, '!=', y, 'adalah', hasil)

# > < >= <= == != ini adalah perbandingan Literal
# x = 4, 4 = Literal (tidak memakan memory)
# x = object (memory)

# Sama "is"
hasil = x is y
print(x, 'is', y, 'adalah', hasil)

# Sama "is not"
hasil = x is not y
print(x, 'is not', y, 'adalah', hasil)