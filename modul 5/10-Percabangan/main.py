# percabangan
# menggunakan statment if

# struktur
"""
    1. if-nya
    2. ada kondisi (bernilai TRUE/FALSE)
    3. ada aksi -> proses lanjutan
"""

nama = input("masukan nama anda = ")

# IF statment dalam bentuk inline (satu baris)
# if nama == "adam": print(f"selamat datang {nama}")
  # Kondisi         # Aksi
# print("terima kasis")

# IF statmen dalam bentuk indentasi
#if nama == 'adam':
    #print(f'selamat datang {nama}')
#print("terima kasih")

# IF-ELSE Statment
if nama == 'adam':
    # aksi 1
    print(f'selamat datang {nama}')
else:
    # aksi 2
    print(f'kamu {nama}, bukan adam')
print('terima kasih')

