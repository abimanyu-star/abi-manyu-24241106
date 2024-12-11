# menggunakan data integer
total_belanja = int(input("Masukkan total belanja Anda (dalam Rupiah): "))

# percabangan
if total_belanja > 500_000:
    bonus = "Mouse dan Keyboard"
else:
    bonus = "Gantungan Kunci"

# Hasil
print(f"Total belanja: Rp{total_belanja:,}")
print(f"Bonus yang didapat: {bonus}")