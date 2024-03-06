"""
Program perulangan menonton DVD dengan menggunakan WHILE
"""

jumlahDVD = 15
print("Tonton DVD-mu")

telahDitonton = 0
print(f"Jumlah DVD yang telah ditonton {telahDitonton} judul")

print("Dengan while")
while telahDitonton < jumlahDVD:
    telahDitonton = telahDitonton + 1
    print(f"DVD ke {telahDitonton} telah ditonton.")

print(f"Jumlah DVD yang telah ditonton {telahDitonton} judul")