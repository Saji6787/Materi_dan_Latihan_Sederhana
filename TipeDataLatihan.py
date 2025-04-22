#=[Soal 1]=
# Diberikan data berikut:
#buah = ['apel', 'mangga', 'jeruk']
#sayur = ('wortel', 'kangkung', 'bayam')

# Tuliskan kode untuk:
# 1. Ubah 'mangga' menjadi 'pisang' dalam list buah
#Jawaban:
#buah[1] = 'pisang'
#print(buah)

# 2. Tambahkan 'anggur' ke akhir list buah
#Jawaban:
#buah.append('anggur')
#print(buah)

# 3. Cobalah ubah 'kangkung' menjadi 'selada' dalam tuple sayur (apa yang terjadi?)
#Jawaban:
#sayur[1] = 'selada'
#print(sayur)
#Akan berakhir error karena tipe data tuple tidak bisa ditambah objek saat program sedang dieksekusi.

# 4. Buatlah list baru yang merupakan gabungan buah dan sayur
#Jawaban:
#print(buah, sayur)

#- - - - - -#

#=[Soal 2]=

# Diberikan data berikut:
#A = {1, 2, 3, 4, 5}
#B = {4, 5, 6, 7, 8}
#mahasiswa = {'nama': 'Rina', 'nim': '12345', 'prodi': 'Informatika'}

# Tuliskan kode untuk:
# 1. Cari irisan (intersection) antara set A dan B
# Jawaban:
#Terdapat dua irisan dalam set A dan B, yaitu 4 dan 5.

# 2. Tambahkan nilai 9 ke set A
#Jawaban:
#A.add(9)
#print(A)

# 3. Ubah nilai 'prodi' mahasiswa menjadi 'Sistem Informasi'
#Jawaban:
#mahasiswa['prodi'] = "Sistem Informasi"

# 4. Hapus key 'nim' dari dictionary mahasiswa
#Jawaban:
#mahasiswa.pop('nim')
#print(mahasiswa)

# 5. Cetak semua key yang ada dalam dictionary mahasiswa
#Jawaban:
#print(mahasiswa)

#- - - - - -#

#=[Soal 3]=
# Diberikan data berikut:
data_str = "3,5,7,9,11"
angka = range(1, 10)

# Tuliskan kode untuk:
# 1. Konversi data_str menjadi list of integers
# 2. Buat range baru untuk angka genap antara 0-20
# 3. Konversi range angka menjadi list
# 4. Hitung jumlah elemen dalam range angka tanpa mengkonversinya ke list
# 5. Buat dictionary yang memetakan setiap angka dalam range(5) ke pangkat duanya