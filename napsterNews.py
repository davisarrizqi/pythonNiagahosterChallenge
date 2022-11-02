'''
Studi Kasus

Skenario --> Pemerintah akan memberikan bantuan bagi mahasiswa
dengan ketentuan parameter IPK minimal 3.30/4.00 dan score
IELTS minimal 5.5.

Skenario 2 --> Pemerintah akan memberikan bantuan senilai
10.000.000 - 15.000.000


Ketentuan Penyelesaian:
1. Menggunakan Fungsi

2. Menggunakan seleksi kondisi

3. Kondisi 1 --> Jika IPK 3.30 - 3.50 dan score IELTS minimal
5.5/9.5 maka bantuan 10.000.000

   Kondisi 2 --> Jika IPK 3.51 - 4.00 dan score IELTS 5.5-9.5
maka bantuan yang akan diberikan sebesar 15.000.000

4. Terdapat main program yang merupakan penerapan fungsi rekursi

5. Gunakan perulangan yang sesuai dengan permasalahan

'''


def penentuanBantuan(IPK, IELTS):
    if (IPK >= 3.30 and IPK <= 3.50):
        if (IELTS >= 5.5):
            print("Bantuan akan diberikan sebesar 10.000.000")

    elif (IPK >= 3.51 and IPK <= 4.00):
        if (IELTS >= 5.5):
            print("Bantuan akan diberikan sebesar 15.000.000")

    else:
        if (IPK < 3.30 and IELTS < 5.5):
            IPK = float(input("IPK tersebut tidak memenuhi syarat, masukkan data IPK baru: "))
            IELTS = float(input("Skor IELTS tersebut tidak memenuhi, masukkan data skor IELTS baru: "))
            penentuanBantuan(IPK, IELTS)

        elif (IPK < 3.30):
            IPK = float(input("IPK tersebut tidak memenuhi syarat, masukkan data IPK baru: "))
            penentuanBantuan(IPK, IELTS)

        elif (IELTS < 5.5):
            IELTS = float(input("Skor IELTS tersebut tidak memenuhi, masukkan data skor IELTS baru: "))
            penentuanBantuan(IPK, IELTS)

        else:
            pass

def main():
    IPK = float(input("Masukkan IPK Anda: "))
    IELTS = float(input("Masukkan Skor IELTS Anda: "))
    penentuanBantuan(IPK, IELTS)

main()
