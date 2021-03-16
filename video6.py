#NIM:71200539
#Nama:Deon Bintang Sanjaya
#Universitas Kristen Duta Wacana

"""
Budi ingin mengunci akun game nya dengan password=130302, namun ia ingin percobaan
password hanya maksimal 3 kali. Buatlah program seperti yang diinginkan Budi
"""
"""
variabel=password
input:
memasukkan password=130302
proses:
pengecekan apakah sesuai dengan password
output:
benar=berhasil
salah3x=exit
"""
password=130302
for i in range(3):
    pass1=int(input("password:"))
    if pass1==password:
        print("Anda berhasil login")
        break
    else:
        pass2=int(input("password:"))
        if pass2==password:
            print("Anda berhasil login")
            break
        else:
            pass3=int(input("password:"))
            if pass3==password:
                print("Anda berhasil login")
                break
            else:
                break

