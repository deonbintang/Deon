#NIM : 71200539 NAMA : DEON BINTANG
#SOAL
#Belvin ingin trading saham dengan profil resiko 1 : 2
#Ia ingin mengetahui berapa keuntungan yang bisa didapat
#Ia juga ingin mengetahui resiko kerugian yang akan terjadi
#Buat sebuah program yang bisa menampilkan apa yang diinginkan Belvin

#P = profit
#L = loss
#U = jumlah uang yang akan ditradingkan
#P1= persenan profit yang diinginkan

#P = U*P1
#L = U*(P1/2)

#Input : Uang : Rp 5000000, profit : 7
#Proses : inputan tersebut akan diproses ke dalam rumus diatas
#Output : hasil keuntungan & kerugian

U = int(input("Jumlah uang yang ingin ditradingkan : Rp"))
P1 = float(input("profit yang diinginkan(dalam persen) :"))
P=U*(P1/100)
L=U*((P1/100)/2)
print("Jadi profit yang bisa didapat = Rp",P,"dengan resiko kerugian = Rp",L)

