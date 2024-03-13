
print('\nPerintah del')
daftarBuku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
del daftarBuku[0]
for i in range(0, len(daftarBuku)):
    print(daftarBuku[i])

print('\nPerintah del dengan list comprehension')
daftarBuku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
del daftarBuku[:] # start:stop, contoh disamping berarti menghapus semua elemen
for i in range(0, len(daftarBuku)):
    print(daftarBuku[i])

print('\nPerintah del dengan list comprehension start')
daftarBuku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
del daftarBuku[0:-1] # start:stop, contoh disamping berarti menghapus semua elemen
for i in range(0, len(daftarBuku)):
    print(daftarBuku[i])

print('\nPerintah del dengan list comprehension step')
daftarBuku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
del daftarBuku[0::3] # start:stop:step, contoh disamping berarti menghapus elemen 0 dan 3.
for i in range(0, len(daftarBuku)):
    print(daftarBuku[i])

print('\nMembuat list baru')
daftarBuku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
daftarBukuBaru = daftarBuku[:]
for i in range(0, len(daftarBuku)):
    print(daftarBuku[i])
del daftarBuku[:]

print('\nHasil delete elements')
for i in range(0, len(daftarBukuBaru)):
    print(daftarBukuBaru[i])

print('\nMembuat list baru dengan comprehension')
daftarBuku = ['1. Seven Habits', '2. How to Influence People', '3. First Things First', '4. 4DX']
daftarBukuBaru = daftarBuku[2::-1] # start:stop:step, mengambil elemen ke-3 hingga awal list.
for i in range(0, len(daftarBukuBaru)):
    print(daftarBukuBaru[i])
print(daftarBuku[0::2]) # shortcut