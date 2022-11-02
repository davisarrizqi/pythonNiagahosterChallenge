'''
Studi Kasus

1. Hapus "Semangka" di dalam listBuah
2. Ubahlah "Anggur" dan "Nanas" menjadi "Melon" dan "Jeruk"
3. Tambahkan "Mangga" dan "Delima" ke dalam listBuah2
4. Gabungkan item yang ada di listBuah2 ke dalam listBuah
5. Sisipkan "Semangka" di antara "Jeruk" dan "Mangga"
6. Urutkan item pada listBuah sesuai abjad
7. Tampilkan buah yang berawalan "m" di dalam listBuah
8. Buatlah function "buahku" dengan parameter "huruf" yang
   akan me-return-kan list yang berisi nama buah yang mengandung 
   huruf "a"
9. Buatlah agar list "matrik" dapat tampil seperti berikut:
   Matrik:
   3  -2   1
  -1   4   7

'''

listBuah = ["Semangka", "Anggur", "Nanas"]
listBuah2 = []
matrik = [[3, -2, 1], [-1, 4, 7]]

# Menghapus "Semangka" di dalam listBuah
counter = 0
for element in listBuah:
    if (element == "Semangka"):
        del listBuah[counter]
    counter += 1
# print(listBuah) --> Debug Hasil


# Mengubah "Anggur" menjadi "Melon" dan "Nanas" menjadi "Jeruk"
counter = 0
for element in listBuah:
    if (element == "Anggur"): listBuah[counter] = "Melon"
    elif (element == "Nanas"): listBuah[counter] = "Jeruk"
    else: pass
    counter += 1
# print(listBuah) --> Debug Hasil


# Menambahkan "Mangga" dan "Delima" ke dalam listBuah2
buahTambahan = ["Mangga", "Delima"]
for buah in buahTambahan:
    listBuah2.append(buah)
# print(listBuah2) --> Debug Hasil


# Menggabungkan item yang ada di listBuah2 ke dalam listBuah
for buah in listBuah2:
    listBuah.append(buah)
# print(listBuah) --> Debug Hasil


# Menyisipkan "Semangka" di antara "Jeruk" dan "Mangga"
indexPosition = 0
for element in listBuah:
    indexPosition += 1
    if (element == "Jeruk"):
        break
listBuah.insert(indexPosition, "Semangka")
# print(listBuah) --> Debug Hasil


# Mengurutkan item pada listBuah sesuai abjad
listBuah.sort()
# print(listBuah) --> Debug Hasil


# Menampilkan buah yang berawalan "m" di dalam listBuah
for element in listBuah:
    if (element[0] == "m" or element[0] == "M"):
        print(element)


# Membuat function "buahku", parameter "huruf"
# return list berisi nama buah mengandung "a"
def buahku(huruf):
    listBaru = [];
    for items in listBuah:
        for alpha in items:
            if (alpha == huruf):
                if (items not in listBaru) : listBaru.append(items)
    return listBaru
listBuahku = buahku('a')  # --> Memasukkan value pada variabel


