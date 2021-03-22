#NIM:71200539
#Nama:Deon Bintang Sanjaya
#Universitas Kristen Duta Wacana
"""
Reiner ingin membuat sebuah program pendaftaran ID untuk giveaway yang akan diadakannya.
Namun Ia memiliki ketentuan untuk ID tersebut yaitu tidak boleh memakai huruf kapital dan spasi
buatlah program seperti yang diinginkan Reiner
"""
"""
Input:
memasukkan ID:reiner777
Proses:
ID akan dicek apakah terdapat spasi ataupun karakter yang berhuruf kapital
Output:
ID bisa digunakan
ID tidak bisa digunakan
"""
nama=str(input("ID:"))
spasi=" "
if nama[0:].islower() and spasi not in nama:
    print("ID anda adalah"+" "+nama)
else:
    print("ID"+" "+nama+" "+"tidak dapat digunakan")