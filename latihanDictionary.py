'''
STUDI KASUS
1. Tampilkan prodi dari data dictionary tersebut
2. Tambahkan "hobi" ke dalam dictMahasiswa dengan value "Menghayal"
3. Hapuslah "alamat" pada dictMahasiswa
4. Isilah list dataMahasiswa dengan dictMahasiswa
5. Tambahkan data berikut ke dalam dataMahasiswa
    "nim" : "5220411002",
    "nama" : "oktavia",
    "prodi" : "arsitektur",
    "hobi" : "menyanyi"    
6. Ubahlah data mahasiswa yang hobinya "menghayal" menjadi "coding"
7. Tampilkan hanya nim dan nama dari data yang ada dalam dataMahasiswa
    Contoh Output:
        "NIM  xxxx dengan nama xxxx"
        "NIM  xxxx dengan nama xxxx"
8. Butalah function "mahasiswaIF", yang hanya akan
menampilkan nama mahasiswa dari profi informatika,
jika diberikan argumen "informatika"
9. Buatlah function "tambahData" yang akan menambahkan
data yang diinputkan oleh pengguna ke dalam dataMahasiswa

'''

from calendar import day_abbr


dictMahasiswa = {
    "nim" : "5220411001",
    "nama" : "rismawan",
    "prodi" : "informatika",
    "alamat" : "yogyakarta"
}

dataMahasiswa = []

# Tampilkan prodi dari data dictionary tersebut
print(dictMahasiswa["prodi"])

# Tambahkan "hobi" ke dalam dictMahasiswa dengan value "Menghayal"
dictMahasiswa["hobi"] = "menghayal"
# print(dictMahasiswa["hobi"]) --> debug hasil

# Hapus "alamat" pada dictMahasiswa
del dictMahasiswa["alamat"]
# print(dictMahasiswa) --> debug hasil

# Mengisi list dataMahasiswa dengan dictMahasiswa
dataMahasiswa = [dictMahasiswa,]
# print(dataMahasiswa) --> debug hasil

# Tambahkan data berikut ke dalam dataMahasiswa
dictMahasiswaOktavia = {
    "nim" : "5220411002",
    "nama" : "oktavia",
    "prodi" : "arsitektur",
    "hobi" : "menyanyi"    
}; dataMahasiswa.append(dictMahasiswaOktavia)
# print(dataMahasiswa) --> debug hasil

# Mengubah "menghayal" menjadi "coding"
if dictMahasiswa["hobi"] == "menghayal": dictMahasiswa["hobi"] = "coding"
# print(dictMahasiswa) --> debug hasil

# Menampilkan hanya nim dan nama dari data yang ada dalam dataMahasiswa
for element in dataMahasiswa:
    nimData = element['nim']; namaData = element['nama']
    # print(f'NIM {nimData} dengan Nama {namaData}') --> debug hasil


# Membuat function mahasiswaIF, menampilkan nama jika argumen "informatika"
def mahasiswaIF(prodi):
    counter = 1
    if (prodi == 'informatika'):
        print("Nama mahasiswa informatika: ")
        for element in dataMahasiswa:
            if (element['prodi'] == 'informatika'):
                print(counter,'). ', element['nama'], sep='')
                counter += 1
# mahasiswaIF('informatika') --> debug pemanggilan


# Membuat function "tambahData" yang akan menambahkan data yang diinputkan oleh pengguna ke dalam dataMahasiswa
def tambahData():
    dataTambahan = {
        "nim" : "",
        "nama" : "",
        "prodi" : "",
        "hobi" : ""    
    }

    for data in dataMahasiswa:
        listData = list(dictMahasiswa.keys())

    for data in range(len(dataTambahan)):
        pilihanInput = listData[data]
        valueInput = input(f'Masukkan {pilihanInput} anda: ')
        dataTambahan.update({pilihanInput: valueInput})

    return dataTambahan

def tambahkanData():
    dataMahasiswa.append(tambahData())

'''
tambahkanData()
print(dataMahasiswa) --> debug hasil
'''
