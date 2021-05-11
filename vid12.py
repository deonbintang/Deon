#NIM:71200539
#Nama:Deon Bintang Sanjaya
#Universitas Kristen Duta Wacana
"""
Robert diberikan 2 set oleh gurunya, set pertama berisi 10,20,30,40,50,60
dan set kedua berisi 20,40,60,80,100,120. Ia diminta untuk menuliskan
hasil-hasil operasi dari kedua set tersebut.
Buatlah program yang dapat membantunya

input:set yang sudah berisi angka-angka
memilih menu yang sudah dibuat
proses:set akan dioperasikan sesuai menu yang dipilih
output:hasil dari operasi
"""
set1={110,20,30,40,60}
set2={20,40,60,800,100,120}
print("1.Union")
print("2.Intersection")
print("3.Difference")
print("4.Symmetric Difference")
print("5.Exit")
while True:
    pil=int(input("Masukkan pilihan:"))
    if pil==1:
        print(set1|set2)
    elif pil==2:
        print(set1&set2)
    elif pil==3:
        print(set1-set2)
    elif pil==4:
        print(set1^set2)
    elif pil==5:
        break