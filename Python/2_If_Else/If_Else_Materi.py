#If ELse

#- - - - - -#

#[ if ] 
#Penjelasan:
#If merupakan sebuah kondisi di mana program akan berjalan jika suatu syarat terpenuhi.

# Contoh: 

'''
a = 9
b = 5

if a > b:
    print("variabel a lebih besar daripada variabel b")
'''
    
#Dalam contoh di atas, variabel a memiliki nilai 9, dan variabel b memiliki nilai 5. Lalu terdapat sebuah syarat IF a > b, yang memiliki arti: jika variabel a lebih besar daripada variabel b, maka akan memunculkan pesan "variabel a lebih besar daripada variabel b".

#- - - - - -#

#[ elif ]
#Penjelasan:
#Elif merupakan sebuah kondisi lanjutan dari if. Cara kerjanya juga sama dengan if. Elif merupakan syarat lanjutan jika kondisi if tidak terpenuhi.

# Contoh:

'''
a = 33
b = 33

if a > b:
    print('variabel a lebih besar daripada variabel b')
elif a == b:
    print('variabel a dan b adalah setara')
'''
    
#Dalam contoh di atas, variabel a memiliki nilai 33, dan variabel b memiliki nilai yang sama yaitu 33. Lalu terdapat 2 syarat, yaitu if dan elif. 

#   pada syarat if disebutkan bahwa jika variabel a lebih besar daripada variabel b, maka akan menunjukkan pesan "variabel a lebih besar daripada variabel b".

#   Sementara pada syarat elif disebutkan bahwa jika variabel a mempunyai nilai yang sama dengan variabel b, maka akan memunculkan pesan "variabel a dan b adalah setara".

#- - - - - -#

#[ else ]
#Penjelasan:
#Else merupakan sebuah kondisi yang bisa saya sebut kondisi akhir, yang berarti jika semua kondisi di atas else tidak terpenuhi, maka kondisi else akan berjalan.

#Contoh:

'''
a = 0
b = 5

if a > b:
    print("variabel a lebih besar daripada variabel b")
else:
    print("nilai variabel tidak memenuhi syarat if")
'''

#Dalam contoh di atas, variabel a meiliki nilai 0 dan variabel b memiliki nilai 5. Lalu terdapat syarat if a > b. Syarat itu menyebutkan bahwa jika variabel a meiliki nilai variabel yang lebih besar daripada b, maka akan memunculkan pesan "variabel a lebih besar daripada variabel b"

#   Sedangkan syarat kedua, yaitu else, memiliki arti: Jika syarat if tidak terpenuhi, maka munculkan pesan "nilai variabel tidak memenuhi syarat"
    
