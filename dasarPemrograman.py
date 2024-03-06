"""
Semua sintaksis dasar pemrograman terdiri dari:
1. Sekuensial   : langkah berurutan.
2. Percabangan  : langkah melompat jika kondisi terpenuhi.
3. Perulangan   : mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi.
"""
# Sekuensial
print('Ibu berkata,"Pergi ke toko"')
print('Budi menjawab, "Baik, apa yang harus saya lakukan di toko?"')
print('Ibu menjawab, "Beli satu botol susu, dan jika ada telur beli 6"')
print("Maka Budi berangkat ke toko")
print("Dan mulai berbelanja")

# Percabangan
jumlahBotolSusu = 200
jumlahTelur = 1500
print(f"Jumlah botol susu {jumlahBotolSusu} botol")
print(f"Jumlah telur {jumlahTelur} butir")

if jumlahBotolSusu > 0:
    print("Budi mengecek harganya dan ternyata uangnya cukup")
    if jumlahTelur == 0:
        print("Budi membeli 1 botol susu")
    else:
        print("Budi membeli 6 botol susu")
else:
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi pulang ke rumah")
print("Kemudian melapor kepada ibu")