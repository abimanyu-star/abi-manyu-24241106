# percabangan bersarang - Nested if

# kalkulator sederhana
print(20*"=")
print ("kalkulator sedeerhana")
print(20*"=")

angka_1 = float(input("masukan angka ke-1 = "))
operator = input("operator (+,-) = ")
angka_2 = float(input("masukan angka ke-2 = "))

# percabangan 
if operator == '+':
    hasil = angka_1 + angka_2
    print(f"Hasilnya adalah = {hasil}")
elif operator == '-':
    hasil = angka_1 - angka_2
    print(f"Hasilnya adalah = {hasil}")
else:
    print("tolong masukan angka dan operator yang benar")