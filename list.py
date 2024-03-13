daftarBuku = ['Seven Habits', 'How to Influence People', 'First Things First']
print(daftarBuku)

print("\nProses semua buku dengan for in")
for buku in daftarBuku:
    print(buku)

print("\nTampilkan daftar buku elemen pertama")
print(daftarBuku[0])

print("\nTampilkan dengan for in range")
for i in range(0, len(daftarBuku)):
    print(daftarBuku[i])

daftarBuku = [1, 'Kenju Volume 2', -313, 3.14]
print("\nTampilkan dengan for in range, dimana tipe data tiap elemen berbeda-beda")
for i in range(0, len(daftarBuku)):
    print(daftarBuku[i])

print("Kembalikan nilai awal daftar buku")
daftarBuku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
print('Tambahkan satu buku baru')
daftarBuku.append('Atomic Habits')

for i in range(0, len(daftarBuku)):
    print(daftarBuku[i])