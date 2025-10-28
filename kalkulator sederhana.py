# Kalkulator Sederhana

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Tidak bisa dibagi dengan nol!"
    return a / b
    

print("=== Kalkulator Sederhana ===")
print("Pilih operasi:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

# Input pilihan pengguna
pilihan = input("Masukkan pilihan (1/2/3/4): ")

# Input angka
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

if pilihan == '1':
    print(f"Hasil: {angka1} + {angka2} = {tambah(angka1, angka2)}")
elif pilihan == '2':
    print(f"Hasil: {angka1} - {angka2} = {kurang(angka1, angka2)}")
elif pilihan == '3':
    print(f"Hasil: {angka1} * {angka2} = {kali(angka1, angka2)}")
elif pilihan == '4':
    print(f"Hasil: {angka1} / {angka2} = {bagi(angka1, angka2)}")
else:
    print("Pilihan tidak valid!")