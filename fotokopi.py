print("Apakah pelanggan (ya/tidak): ")
pelanggan = input()

print('Jumlah fotokopi: ')
jumlah = input()

if pelanggan == 'ya' :
    harga = int(jumlah)*75
    print(f"harga fotokopi adalah {harga}")
else :
    if int(jumlah) < 100 :
        harga = int(jumlah) * 150
        print(f"harga fotokopi adalah {harga}")
    elif int(jumlah) >= 100 and int(jumlah) <= 200 :
        harga = int(jumlah) * 100
        print(f"harga fotokopi adalah {harga}")
    else :
        harga = int(jumlah) * 80
        print(f"harga fotokopi adalah {harga}")