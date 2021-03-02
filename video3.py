#Nama : Deon Bintang Sanjaya
#NIM : 71200539
#Universitas Kristen Duta Wacana

"""Benny ingin membeli suatu saham melalui sekuritas IndoReguler, IndoReguler sendiri menerapkan
fee beli sebesar 0,24%. Buatlah sebuah fungsi dimana Benny bisa mengetahui jumlah akhir
yang harus dibayarkan"""

"""
a=harga saham
b=jumlah lembar
Input =
a=800
b=1000
Proses=
harga=a*b+fee
Output=
jumlah akhir
"""
def hargafix(a,b):
    total=(a*b)+(a*b*0.0024)
    return total
a=int(input("Masukkan harga saham:"))
b=int(input("Jumlah lembar saham:"))
print("Jumlah akhir yang harus dibayar yaitu",hargafix(a,b))





