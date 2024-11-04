# Meminta pengguna untuk memasukkan bilangan
bilangan = int(input("Masukkan bilangan: "))

# Menentukan apakah bilangan tersebut ganjil atau genap
if bilangan % 2 == 0:
    print(f"{bilangan} adalah bilangan genap.")
else:
    print(f"{bilangan} adalah bilangan ganjil.")