def hitungLuas():
    Inputpanjang = input('masukan panjang')
    Inputlebar = input('masukan lebar')
    luas = int(Inputpanjang) * int(Inputlebar)
    print(luas)

def luasLingkaran():
    phi = 3.14
    jari = input('masukan angka')
    luas = (int(jari) ** 2) * phi
    print(luas)

def hitungRata() :
    print('rata-rata')
    data = []
    inputUser = 0
    while True:
        inputUser = input("masukan angka")
        if inputUser == 'n':
            break
        data.append(int(inputUser))
        total = 0
    for i in data:
        total += i

    b = len(data)
    c = total / b
    print('rata-rata =', c)
    print('total=', total)

def GanjilGenap():
    inputUser = input('masukan angka')
    if int(inputUser) % 2 == 0:
        print('genap')
    else:
        print('ganjil')

def selesai() :
    print('selesai')

def tampilkanMenu() :
    #tampilan menu
    print('='*100)
    print('menu pilihan')

    data = [
        {"nama": '1.Luas Persegi Panjang', 'fungsi': hitungLuas},
        {'nama': '2.Luas Lingkaran', 'fungsi': luasLingkaran},
        {'nama': '3.Menghitung rata-rata', 'fungsi': hitungRata},
        {'nama':'4.Menghitung ganjilGenap', 'fungsi': GanjilGenap},
        {'nama': '5.Selesai', 'fungsi': selesai}
    ]
    for x in data:
        print(f"{x['nama']}")

    jawaban =input("masukan angka yang ingin di tampilkan")

    data[int(jawaban)-1]['fungsi']()
    tampilkanMenu()


tampilkanMenu()
