# Program: Perhitungan Harga Tiket Bioskop
# Bahasa: Python

print("=== Program Harga Tiket Bioskop ===")

# Daftar harga tiket menggunakan list
jenis_tiket = ["Regular", "VIP"]
harga_tiket = [50000, 100000]

# Tampilkan daftar harga
print("\nDaftar Harga Tiket:")
for i in range(len(jenis_tiket)):
    print(f"{i+1}. {jenis_tiket[i]} - Rp{harga_tiket[i]:,}")

# Pilihan jenis tiket
pilihan = int(input("\nPilih jenis tiket (1/2): "))

if pilihan < 1 or pilihan > len(jenis_tiket):
    print("Pilihan tidak valid!")
    exit()

# Ambil harga tiket berdasarkan pilihan
tiket_dipilih = jenis_tiket[pilihan - 1]
harga = harga_tiket[pilihan - 1]

# Input jumlah tiket
jumlah = int(input("Masukkan jumlah tiket yang ingin dibeli: "))

# Cek status member
member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").lower()

# Diskon untuk member
if member == "ya":
    diskon = 0.2  # 20% diskon untuk member
else:
    diskon = 0.0

# Hitung total
subtotal = harga * jumlah
potongan = subtotal * diskon
total_bayar = subtotal - potongan

# Tampilkan hasil
print("\n=== Rincian Pembelian ===")
print(f"Jenis tiket: {tiket_dipilih}")
print(f"Harga per tiket: Rp{harga:,}")
print(f"Jumlah tiket: {jumlah}")
print(f"Status member: {'Ya' if member == 'ya' else 'Tidak'}")
print(f"Diskon: {diskon*100:.0f}%")
print(f"Total yang harus dibayar: Rp{total_bayar:,.0f}")

print("\nTerima kasih telah membeli tiket di bioskop kami!")