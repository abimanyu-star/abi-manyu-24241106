import math

# Fungsi untuk menghitung luas lingkaran
def hitung_luas_lingkaran(r):
    return math.pi * (r ** 2)

# Menggunakan nilai jari-jari default r = 11.5
default_r = 11.5
print(f"Nilai jari-jari default adalah: {default_r}")

# Tempat untuk input dari pengguna
input_user = input("Masukkan nilai jari-jari lingkaran (r) atau tekan Enter untuk menggunakan nilai default (11.5): ")

# Jika pengguna tidak memasukkan nilai, gunakan nilai default
if input_user.strip() == "":
    r = default_r
else:
    r = float(input_user)

# Menghitung luas
luas = hitung_luas_lingkaran(r)

# Menampilkan hasil
print(f"Luas lingkaran dengan jari-jari {r} adalah: {luas:.2f}")
