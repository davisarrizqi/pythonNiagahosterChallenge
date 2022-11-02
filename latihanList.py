'''
Studi Kasus

1. Hapus "Semangka" di dalam listBuah
2. Ubahlah "Anggur" dan "Nanas" menjadi "Melon" dan "Jeruk"
3. Tambahkan "Mangga" dan "Delima" ke dalam listBuah2
4. Gabungkan item yang ada di listBuah2 ke dalam listBuah
5. Sisipkan "Semangka" di antara "Jeruk" dan "Mangga"
6. Urutkan item pada listBuah sesuai abjad
7. Tampilkan buah yang berawalan "m" di dalam listBuah
8. Buatlah function "buahku" dengan parameter

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


# Membuat function "buahku" dengan parameter untuk menginput pada listBuah
def buahku(namaBuah):
    listBuah.append(namaBuah)
buahku("Buah Bibir")
print(listBuah)
