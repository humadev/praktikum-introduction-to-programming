# ============ ============ ============ soal no 1

# deklarasi array
mahasiswa = ['pras', 'jo', 'si C', 'si D', 'si E']

# menghitung jumlah elemen pada array
jumlahMahasiswa = len(mahasiswa)

# menampilkan elemen dan jumlah pada array
print(mahasiswa, 'berjumlah', jumlahMahasiswa)

# ============ ============ ============ soal no 2

# menampilkan pertanyaan dan mengambil input dari user
pilih = input('pilih index mahasiswa yg akan ditampilkan :')

# casting input user dari string menjadi integer
pilihInt = int(pilih)

# memvalidasi apakah index yang diinput user ada pada array
if(pilihInt < jumlahMahasiswa) :
    print('nama mahasiswa ', mahasiswa[pilihInt])
else :
    print('index tidak ditemukan!')


# ============ ============ ============ soal no 3
# menampilkan pertanyaan dan mengambil input dari user
tambah = input('masukkan nama mahasiswa : ')

mahasiswa.append(tambah)

print(mahasiswa)

# ============ ============ ============ soal no 4
# menampilkan pertanyaan dan mengambil input dari user
hapus = input('masukkan index mahasiswa yang akan dihapus: ')
# casting input user dari string menjadi integer
hapusInt = int(hapus)
mahasiswa.pop(hapusInt)

print(mahasiswa)

# ============ ============ ============ soal no 5
# menampilkan pertanyaan dan mengambil input dari user
indexEdit = input('masukkan index mahasiswa yang akan diedit: ')

# casting input user dari string menjadi integer
indexEditInt = int(indexEdit)

# menampilkan pertanyaan dan mengambil input dari user
edit = input(f'{mahasiswa[indexEditInt]} diganti menjadi? ')
# casting input user dari string menjadi integer

mahasiswa[indexEditInt] = edit

print(mahasiswa)