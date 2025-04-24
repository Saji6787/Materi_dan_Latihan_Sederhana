# [ANSWERS!!!]

# [File ini merupakan file jawaban soal beserta penjelasannya]


# - - - - - - - - - - # - - - - - ///
#[DIFFICULTY: EASY]     - - - - - ///
# - - - - - - - - - - # - - - - - ///



#1. Apa saja tipe data dari variabel berikut?

'''
x = 10
y = "Halo"
z = 3.14
a = True
b = [1, 2, 3]
'''

#Tentukan tipe data (int, str, float, bool, atau list) dari setiap variabel di atas.

# ///////// 
# <ANSWERS>
# ///////// 

'''

x = 10       # int → Bilangan bulat
y = "Halo"   # str → Teks/string
z = 3.14     # float → Bilangan desimal
a = True     # bool → Boolean, hanya dua nilai: True atau False
b = [1, 2, 3] # list → Kumpulan data yang bisa diubah

PENJELASAN:

Python punya beberapa tipe data dasar:
1. int untuk angka bulat
2. float untuk angka desimal
3. str untuk teks
4. bool untuk logika
5. list untuk kumpulan data (seperti array)

'''

# - - - /// - - - #

#2. Ubah nilai berikut menjadi tipe data yang disebutkan:

'''
angka = "25"
'''

#Ubah angka menjadi int, lalu tambahkan 10 dan cetak hasilnya.

# ///////// 
# <ANSWERS>
# ///////// 

'''

angka = "25"       # Sekarang berupa string
angka = int(angka) # Diubah ke angka bulat (int)
hasil = angka + 10
print(hasil)       # Output: 35

PENJELASAN:

Kita bisa ubah string "25" menjadi angka dengan int(). Setelah itu, bisa langsung dijumlahkan.

'''

# - - - /// - - - #

#3. Berikut adalah variabel string:

'''
teks = "Python"
'''

#Cetak huruf pertama dan huruf terakhir dari string teks.

# ///////// 
# <ANSWERS>
# ///////// 

'''
teks = "Python"
print(teks[0])   # Output: P → Huruf pertama
print(teks[-1])  # Output: n → Huruf terakhir

PENJELASAN:

teks[0] artinya ambil karakter ke-1 (indeks dimulai dari 0)
teks[-1] artinya ambil karakter terakhir (negatif berarti dari belakang)


'''

# - - - /// - - - #

#4. Diberikan list berikut:

'''
buah = ["apel", "jeruk", "mangga"]
'''

# a. Tambahkan "pisang" ke dalam list.
# b. Cetak list setelah ditambahkan.

# ///////// 
# <ANSWERS>
# ///////// 

'''
buah = ["apel", "jeruk", "mangga"]
buah.append("pisang")  # Menambah item ke list
print(buah)
# Output: ['apel', 'jeruk', 'mangga', 'pisang']

PENJELASAN:
Fungsi .append() digunakan untuk menambahkan data ke akhir list.
'''

# - - - /// - - - #

#5. Apa perbedaan utama antara tuple dan list di Python?
# Berikan contohnya juga.

# ///////// 
# <ANSWERS>
# ///////// 

'''
# List → bisa diubah
buah_list = ["apel", "jeruk"]
buah_list[0] = "pisang"  # OK, bisa diganti

# Tuple → tidak bisa diubah
buah_tuple = ("apel", "jeruk")
# buah_tuple[0] = "pisang" → ERROR: karena tuple bersifat tetap

PENJELASAN:

list bisa diubah isinya (mutable)
tuple tidak bisa diubah setelah dibuat (immutable)


'''

# - - - - - - - - - - # - - - - - ///
#[DIFFICULTY: MEDIUM]   - - - - - ///
# - - - - - - - - - - # - - - - - ///



#1. Diberikaan list berikut:

'''
angka = [1, 2, 3, 2, 4, 1, 5]
'''

#Hapus semua duplikat dari list tersebut dan cetak hasil akhirnya.

# - - - /// - - - #

#2. Diberikan dictionary sebagai berikut:

'''
murid = {
    "Ani": 85,
    "Budi": 90,
    "Citra": 78
}
'''

#Berdasarkan data di atas:
# A. Tambahkan data murid baru bernama "Dedi" dengan nilai 88.
# B. Ubah nilai "Ani" menjadi 92.
# C. Cetak dictionary setelah perubahan.

# - - - /// - - - #

#3. Buat list baru yang berisi kuadrat dari angka genap dari list berikut:

'''
angka = [1, 2, 3, 4, 5, 6]
'''

# - - - /// - - - #

#4. Diberikan struktur data cammpuran sebagai berikut:

'''
data = {
    "nama": "Fajar",
    "nilai": [80, 85, 90],
    "aktif": True
}
'''

#Berdasarkan data di atas:
# A. Tambahkan nilai 95 ke list nilai.
# B. Hitung rata-rata nilai.
# C. Cetak hasilnya.

# - - - /// - - - #

#5. Diberikan tuple:

'''
info = ("Andi", 17, "Jakarta")
'''

#Gunakan tuple unpacking untuk menyimpan nilai ke dalam variabel nama, umur, dan kota, lalu cetak dalam format:
#   Nama: Andi, Umur: 17, Kota: Jakarta



# - - - - - - - - - - # - - - - - ///
#[DIFFICULTY: HARD]     - - - - - ///
# - - - - - - - - - - # - - - - - ///



#1. Diberikan data berikut:

'''
kelas = {
    "kelasA": {
        "Ani": 85,
        "Budi": 90
    },
    "kelasB": {
        "Citra": 88,
        "Dedi": 92
    }
}
'''

# A. Tambahkan murid "Eka" dengan nilai 87 ke kelasA.
# B. Hitung total rata-rata nilai dari semua murid di semua kelas.

# - - - /// - - - #

#2. Diberikan list berikut:

'''
data = [
    {"nama": "Ari", "nilai": 78},
    {"nama": "Bima", "nilai": 85},
    {"nama": "Cici", "nilai": 90}
]
'''

# A. Buat list nama murid yang nilainya di atas 80
# B. Hitung rata-rata nilai dari seluruh murid.

# - - - /// - - - #

#3. Diberikan dua data set berikut:

'''
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
'''

# A. Cetak irisan (intersection) dari a dan b.
# B. Cetak gabungan (union) dari a dan b
# C. Cetak selisih (difference) dari a terhadap b.

# - - - /// - - - #

#4. Diberikan data berikut:

'''
data = [
    ("Ari", {"math": 90, "english": 85}),
    ("Bima", {"math": 80, "english": 88}),
    ("Cici", {"math": 85, "english": 90}),
]
'''

# A. Buat dictionary baru dengan nama murid sebagai kunci dan rata-rata nilai sebagai nilai.
# B. Cetak dictionary tersebut.

# - - - /// - - - #

#5. Diberikan list campuran berikut:

'''
data = [10, "20", 30.5, "40.5", True, "abc"]
'''

# A. Buat list baru yang hanya berisi angka (baik int maupun float).
# B. Konversi angka yang berupa string menjadi tipe numerik.
# C. Hitung total seluruh angka.


