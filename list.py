# Contoh penggunaan list di Python
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

print('\nClear List')
daftarBuku.clear()
for i in range(0, len(daftarBuku)):
    print(daftarBuku[i])

print('\nGanti elemen pertama')
daftarBuku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
daftarBuku[0] = 'Eight Habits'
for i in range(0, len(daftarBuku)):
    print(daftarBuku[i])

print('\nAmbil elemen ke-2')
buku = daftarBuku.pop(1)
for i in range(0, len(daftarBuku)):
    print(daftarBuku[i])

print('\nBuku yang diambil tadi')
print(buku)

print('\nPop')
daftarBuku.pop()
for i in range(0, len(daftarBuku)):
    print(daftarBuku[i])

# Berguna ketika bermain dengan tipe data stack
print('\nPop2')
daftarBuku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
daftarBuku.pop(-1)
for i in range(0, len(daftarBuku)):
    print(daftarBuku[i])