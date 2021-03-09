#NIM:71200539
#Nama:Deon Bintang Sanjaya
#Universitas Kristen Duta Wacana
"""
Kenneth ingin mencari sebuah deret aritmatika, namun ia malas mencari deretan bilangan tersebut
secara manual, buatlah sebuah program yang dapat menampilkan deret aritmatika secara otomatis
"""
"""
Input:
bil awal=1
jumlah deret=10
penambahan=6
Proses:
bil awal+penambahan
sebanyak jumlah deret yang diinginkan
Output:
deret aritmatika
"""
try:
    awal=int(input("Masukkan bilangan sebelumnya:"))
    jumlah=int(input("Jumlah deret:"))
    penambahan=int(input("Penambah:"))
    for i in range(0,jumlah):
        awal=awal+penambahan
        print(awal,"",end="")
except:
    print("Silahkan masukkan bilangan integer")
