#NIM:71200539
#nama:Deon Bintang Sanjaya
#Universitas Kristen Duta Wacana
"""Budi adalah seorang siswa yang sedang belajar mengenai pemangkatan,
ia membutuhkan program untuk mencari hasil dari pemangkatan angka.
Bantulah Budi membuat program tersebut menggunakan fungsi rekursif"""
"""
input nama fungsi dan parameter
5 pangkat 4
proses angka di turunkan hingga pangkat menjadi 1 lalu dinaikkan lagi
output hasil dari pemangkatan
"""
def pangkat(a,b):
    if b==0:
        return 1
    elif a==0:
        return 0
    elif b==1:
        return a
    else:
        return a*pangkat(a,b-1)
print(pangkat(10,10))