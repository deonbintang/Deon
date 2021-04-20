#NIM:71200539 #nama:Deon Bintang Sanjaya
#Universitas Kristen Duta Wacana
"""Kenneth ingin membuat sebuah playlist lagu kesukaannya, ia meminta
bantuanmu untuk membuatkan program yang bisa membantunya menggunakan list
"""
"""
input:lagu-lagu(bebas)
proses:lagu tersebut dimasukkan ke dalam list
output:playlist yang berisi lagu yang diinput
"""
daftar=[]
stop=False
i=0
while not stop:
    lagu=input("Masukkan lagu yang diinginkan:".format(i))
    daftar.append(lagu)
    i+=1
    ask=input("Tambahkan lagi?(y/n)")
    if ask=="n":
        stop=True
print("Daftar lagumu yaitu",daftar)
