print('Masukan Jam : ')
jam= input()

if int(jam) >= 3 and int(jam) <= 10 : print('Selamat Pagi')
elif int(jam) >= 11 and int(jam) <= 14 : print('Selamat Siang')
elif int(jam) >= 15 and int(jam) <= 18 : print('Selamat Sore')
elif int(jam) >= 19 and int(jam) <= 24 : print('Selamat malam')
else : print('angka ini bukan jam')