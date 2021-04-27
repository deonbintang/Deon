#NIM:71200539
#Nama:Deon Bintang Sanjaya
#Universitas Kristen Duta Wacana
"""
Pak Joko ingin membuat ranking pada kelasnya dengan menggunakan nilai
akhir dari murid-muridnya, ia menginginkan program yang bisa mengurutkan
nilai dari terkecil hingga terbesar menggunakan dictionary

input
nilai-nilai akhir dari semua murid
60,50,100,55,89,24,54,100,78,95
proses
nilai tersebut disorting supaya urut
output
urutan nilai dari kecil ke besar
"""
kelas={"nilai":[75,67,97,95,80,46,70,78,77,89]}
sort={x:sorted(y) for x,y in kelas.items()}
print(sort)