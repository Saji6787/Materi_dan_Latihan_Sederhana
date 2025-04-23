#Data Types

DataType_string   = "Hello, World!"
DataType_integer  = 20
DataType_float    = 20.5
DataType_complex  = 5j
DataType_bool     = True

#- - - - - -#

DataType_list     = ["apple", "banana", "grape"]
DataType_tuple    = ("apple", "banana", "grape")
DataType_set      = {"Apple", "banana", "grape"}
DataType_range    = range(5)
DataType_dict     = {"name" : "John", "age" : 36}

#- - - - - -#
#List
#Untuk menyimpan data yang mungkin berubah selama program berjalan.

#Contoh List:
buah = ['apel', 'pisang', 'jeruk']
buah.append('mangga')  # Menambah elemen
buah[1] = 'kiwi'       # Mengubah elemen
#print(buah)  # Output: ['apel', 'kiwi', 'jeruk', 'mangga']

#Note: Kenapa pisang tidak terdaftar atau menghilang saat meng-run code? karena bagian yang diubah adalah pisang. buah[1] = 'kiwi' artinya kiwi menggantikan posisi nomor 1 dan menghapus pisang. Kenapa nomor 1 berada di urutan kedua? karena dihitung dari angka 0.

#- - - - - -#

# Tuple
#Memiliki fungsi untuk menyimpan koleksi data yang terurut dan tidak dapat diubah selama program berjalan. Memungkinkan duplikat elemen.

#Contoh Tuple:
koordinat = (10.5, 20.3)
warna_rgb = (255, 128, 0)

# Tidak bisa diubah
# koordinat[0] = 15.0  # Akan error

#- - - - - -#

#Set/Himpunan
#Memiliki fungsi untuk menyimpan koleksi data yang tidak terurut, tidak bisa diindeks, dan tanpa duplikat. Digunakan saat melakukan operasi himpunan yang efisien, saat perlu menyimpan nilai yang unik seperti email, nomor hp, nik, dan lain-lain. Bisa juga digunakan saat melakukan operasi himpunan seperti gabungan, irisan, dll.

#Contoh Set/Himpunan:
unik = {1, 2, 3, 2, 1, 3, 4, 4, 5}  # Duplikat akan dihapus
#print(unik)  # Output: {1, 2, 3, 4, 5}

unik.add(4)  # Menambah elemen
unik.remove(2)  # Menghapus elemen

#- - - - - -#

#Range
    #Berfungsi untuk menghasilkan urutan angka yang tidak dapat diubah. Jenis data ini sering digunakan untuk perulangan. Memiliki efisiensi dalam penggunaan memori dan sangat berguna untuk iterasi dalam loop. Jenis data ini biasanya digunakan saat perlu membuat perulangan dengan jumlah tertentu, bisa juga digunakan saat perlu menghasilkan urutan angka.
    
#Contoh Range:
#for R in range(5):  # 0 sampai 4
    #print(R)

# angka_genap = list(range(0, 10, 2))  # [0, 2, 4, 6, 8]

#- - - - - -#

#Dicitonary
    #Berfungsi untuk menyimpan data dengan label atau identifikasi unik, atau bisa juga berfungsi untuk mengakses data dengan cepat berdasarkan key.
    
#Contoh Dictionary:
#mahasiswa = {
    #'nama': 'Budi',
    #'nim': 'IT250135',
    #'prodi': 'Informatika'
#}

#print(mahasiswa['nama'] + ' ' + mahasiswa['nim'])  # Output: Budi
#mahasiswa['semester'] = 5  # Menambah data

#- - - - - -#

#Practice:

character = {
    'Nama': 'Lisa',
    'Age' : '25',
    'Race': 'Human'
}

if character.get('Nama') == 'Adam':
    print("His name is Adam")
else:
    print("He isn't Adam, his name is" + ' ' + character['Nama'])
