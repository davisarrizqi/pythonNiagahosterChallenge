import random

# Memasukkan semua karakter diizinkan (A-Z)
listHuruf = []; startFrom = 65; into = 90
for napster in range(90-64):
    listHuruf.append(chr(napster + 65))
print('\n')

class TebakHuruf:
    def __init__(self) -> listHuruf:
        self.listHuruf = listHuruf
        self.counter = 1; self.keterangan = ''
        self.listKeterangan = ['Sebelum huruf ini', 'Sesudah huruf ini']
        self.jawaban = ''; self.posisiIndex = 0

    def pusatAplikasi(self):
        # Memasukkan jawaban untuk self.jawaban
        self.posisiIndex = random.randrange(0, len(self.listHuruf) - 1)
        self.jawaban = self.listHuruf[self.posisiIndex]
        inputPengguna = ''

        # Deklarasi teks untuk judul dan notice
        title = 'PERMAINAN TEBAK HURUF A-Z'
        notice = 'Hidupkan CapsLock Pada Keyboard Anda!'
        
        # Menampilkan karakter yang diizinkan
        print('     ', end='')
        for huruf in self.listHuruf:
            print(huruf, end=' ')

        # Menampilkan top-outline-header pada terminal
        print('\n          +', end='')
        for jk in range(len(notice) + 3):
            print('-', end='')
        print('+')

        # Menampilkan text-header pada terminal
        print('          ', title.center(40)); print('          ', notice.center(40))

        # Menampilkan bottom-outline-header pada terminal
        print('          +', end='')
        for jk in range(len(notice) + 3):
            print('-', end='')
        print('+'); print('     ', end='')

        # Menampilkan karakter yang diizinkan
        for huruf in self.listHuruf:
            print(huruf, end=' ')

        # Melakukan looping aplikasi
        while inputPengguna != self.jawaban:
            # Menampilkan top-outline untuk ruang jawaban
            print('\n\n          +', end='')
            for jk in range(len(notice) + 3):
                print('-', end='')
            print('+')

            # Menampilkan hitungan ke berapa
            print(f'          | Ini adalah urutan ke: {self.counter}')

            # Mengisi baris
            kalimatPertanyaan = '          | Tebak Huruf: '
            inputPengguna = input(kalimatPertanyaan)
            
            # Menampilkan keterangan
            myCounter = 0; myPosition = 0
            for element in self.listHuruf:
                if (element == inputPengguna):
                    myPosition = myCounter
                myCounter += 1
            
            if (myPosition > self.posisiIndex):
                self.keterangan = self.listKeterangan[0]
                self.counter += 1

            elif (myPosition < self.posisiIndex):
                self.keterangan = self.listKeterangan[1]
                self.counter += 1

            elif (myPosition == self.posisiIndex):
                self.counter += 1
                self.keterangan = "Jawaban anda benar!, anda mencoba sebanyak "
                self.keterangan += str(self.counter) + " kali"


            else:
                pass

            print(f'          | Keterangan: {self.keterangan}')

            # Menampilkan bottom-outline untuk ruang jawaban
            print('          +', end='')
            for jk in range(len(notice) + 3):
                print('-', end='')
            print('+', end='')

napster = TebakHuruf()
napster.pusatAplikasi()
