def hitung_bmi(berat, tinggi):
    bmi = berat / (tinggi ** 2)
    return bmi

def status_bmi(bmi):
    if bmi < 18.5:
        return "Kurus"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Kegemukan"
    else:
        return "Obesitas"

berat = 65  # kg
tinggi = 1.7  # m

bmi = hitung_bmi(berat, tinggi)
status = status_bmi(bmi)

print(f"Berat: {berat} kg")
print(f"Tinggi: {tinggi} m")
print(f"BMI: {bmi:.1f}")
print(f"Status BMI: {status}")
