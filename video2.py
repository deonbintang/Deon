#Nama : Deon Bintang Sanjaya
#NIM : 71200539
#Universitas Kristen Duta Wacana

"""
Andi ingin membuat program yang ingin digunakan untuk menjual nomor lotre, namun ia hanya
ingin menjual nomor untuk keluaran 2 angka. Bantulah Andi membuat program tersebut
"""
"""
input : memasukkan 2 angka yang akan dibeli
proses :angka tersebut akan diproses pada percabangan if
output :statement yang sesuai dengan angka yang sudah dimasukkan
"""
a=input("Masukkan angka yang akan dibeli:")
try:
    angka=int(a)
    if angka >=0 and angka <= 9:
        print("angka yang anda beli adalah 0",angka)
    elif angka >9 and angka <=99:
        print("angka yang anda beli adalah",angka)
    elif angka >99:
        print("silahkan masukkan 2 angka")
    elif angka <0:
        print("silahkan masukkan 2 angka positif")
except:
    print("data yang anda masukkan tidak valid")


