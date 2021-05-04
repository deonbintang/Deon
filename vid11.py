#NIM:71200539
#Nama:Deon Bintang Sanjaya
#Universitas Kristen Duta Wacana
"""
Bu Rini ingin memisahkan jumlah murid-muridnya berdasarkan gender,
buatlah program tersebut dengan output berupa dictionary

input:jumlah laki-laki & perempuan
laki2=10
perempuan=15
proses:integer tadi digabung dengan string
tuple diconvert menjadi dictionary
output:dictionary berisi gender dan jumlah muridnya
"""
x=int(input("Masukkan jumlah murid laki-laki:"))
y=int(input("Masukkan jumlah murid perempuan:"))
tuples=(("Laki-laki",x),("Perempuan",y))
print(dict(tuples))
