"""
Program perulangan menonton dan memahami makna Film dengan WHILE
"""

jumlahFilm = 10
print("Kamu harus menonton semua Film dan pahami maknanya")

ditonton = 0
dipahami = 0
print(f"Jumlah film yang telah ditonton dan dipahami {dipahami}")

while ditonton < jumlahFilm * 2:
    ditonton = ditonton + 1
    if dipahami == 9:
        print(f"Film ke {dipahami + 1} belum paham")
    else:
        dipahami = dipahami + 1
        print(f"Film ke {dipahami} telah ditonton dan dipahami")

print(f"Jumlah film yang telah ditonton dan dipahami {dipahami}")
if dipahami == jumlahFilm:
    print("Semua film telah ditonton dan dipahami")
else:
    print(f"Tidak semua film bisa dipahami. "
          f"Saya hanya bisa memahami {dipahami} film")

# dynamically static variable
jumlahFilm = 'banyak'
print(jumlahFilm)
