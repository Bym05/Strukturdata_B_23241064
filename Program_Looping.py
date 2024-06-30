# Looping menggunakan for
for i in range(1, 11):
    print(i)
# Looping menggunakan while
i = 1
while i <= 10:
    print(i)
    i += 1
# List buah-buahan
fruits = ["apel", "pisang", "ceri"]

# Looping menggunakan for untuk mencetak setiap elemen dalam list
for fruit in fruits:
    print(fruit)
# Nested loop untuk mencetak tabel perkalian
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print("-" * 10)
# Looping dengan break dan continue
for i in range(1, 11):
    if i == 5:
        continue  # Lewati angka 5
    if i == 8:
        break  # Hentikan loop ketika mencapai angka 8
    print(i)
# Looping menggunakan while dengan break dan continue
i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue  # Lewati angka 5
    if i == 8:
        break  # Hentikan loop ketika mencapai angka 8
    print(i)
    i += 1