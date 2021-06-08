#NIM:71200539
#nama:Deon Bintang Sanjaya
#Universitas Kristen Duta Wacana

"""Tejo meminta bantuan untuk dibuatkan pencarian url menggunakan regex,
bantulah sesuai apa yang diminta Tejo"""
"""
input : teks yang isinya ada url nya
(https://lms.ukdw.ac.id http://eclass.ukdw.ac.id e-learning)
proses :re.findall untuk mencari url 
output : url
"""
import re
teks="https://netflix.com http://games.co.id google.co.id"
cari=re.findall("http[s]?://(?:[a-zA-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",teks)
print("URL:",cari)