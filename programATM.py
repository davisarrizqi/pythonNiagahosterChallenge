"""
Program Sederhana ATM
> 
"""
import os
import time
from datetime import date
hasilInput = 99

def pause():
    os.system('pause')

def clear():
    os.system('cls')

def tarikTunai():
    listKeuangan = [0, 100000, 200000, 300000, 500000, 700000, 1000000, 1250000]
    listPilihanKeuangan = [1, 2, 3, 4, 5, 6, 7]
    print(
        """
        Pilih Jumlah Penarikan Uang:
        1). 100.0000
        2). 200.000
        3). 300.000
        4). 500.000
        5). 700.000
        6). 1.000.000
        7). 1.250.000
        8). Jumlah Lainnya
        0). Kembali Ke Halaman Utama
        """
    ); menuDipilih = int(input("        Pilih yang anda inginkan: "))

    if (menuDipilih in listPilihanKeuangan):
        print("        Melakukan proses output uang fisik..")
        time.sleep(3)
        print(f"        Pengambilan uang sebesar {listKeuangan[menuDipilih]} berhasil!")

    elif (menuDipilih == 8):
        jumlahTransfer = input("        Masukkan jumlah yang anda inginkan: ")
        print(f"        Memulai pengambilan uang sebesar {jumlahTransfer}...")
        time.sleep(3)
        print("        Pengambilan uang berhasil!")

    elif (menuDipilih == 0):
        print("        Kembali ke halaman utama")

    else:
        print("        Input tidak valid, mengulang kembali!")


def transferKeuangan():
    print(
        """
        Pilihan Transfer:
        1). Transfer Antarrekening
        2). Transfer Antarbank
        3). Transfer Diri Sendiri
        """
    ); hasilInput = int(input("        Pilih yang anda inginkan: "))

    if (hasilInput == 1):
        rekeningTujuan = input("        Masukkan nomor rekening tujuan: ")
        namaPemilikRekening = input("        Masukkan atas nama pemilik rekening tujuan: ")
        tanggalSekarang = date.today()
        jumlahTransfer = input("        Masukkan jumlah transfer yang anda inginkan: ")

        print("        Memproses sistem..."); time.sleep(3)
        print(
            f"""
                       DETAIL TRANSFER
            Nomor Tujuan    : {rekeningTujuan}
            Nama Tujuan     : {namaPemilikRekening}
            Jumlah Transfer : Rp{jumlahTransfer},00
            Tanggal         : {tanggalSekarang}
            """
        ); pause()

    elif (hasilInput == 2):
        bankTujuan = input("        Masukkan nama bank tujuan: ")
        rekeningTujuan = input("        Masukkan nomor rekening tujuan: ")
        namaPemilikRekening = input("        Masukkan atas nama pemilik rekening tujuan: ")
        tanggalSekarang = date.today()
        jumlahTransfer = input("        Masukkan jumlah transfer yang anda inginkan: ")

        print("        Memproses sistem..."); time.sleep(3)
        print(
            f"""
                       DETAIL TRANSFER
            Nama Bank Tujuan  : {bankTujuan}
            Nomor Tujuan      : {rekeningTujuan}
            Nama Tujuan       : {namaPemilikRekening}
            Jumlah Transfer   : Rp{jumlahTransfer},00
            Tanggal           : {tanggalSekarang}
            """
        ); pause()

    elif (hasilInput == 3):
        jumlahTransfer = input("        Masukkan jumlah transfer yang anda inginkan: ")
        tanggalSekarang = date.today()

    else:
        print("        Input tidak valid, mengulang kembali!")

def informasiSaldo():
    print("        Saldo Anda")
    print("        Rp1.589.000.101")


while hasilInput != 0:
    clear()
    
    print(
        """
        ----- ATM KITA -----
        1. Tarik Tunai
        2. Transfer
        3. Info Saldo
        0. Keluar
        --------------------
        """
    ); hasilInput = int(input('        Masukkan pilihan: '))

    if (hasilInput == 1):
        tarikTunai(); pause()

    elif (hasilInput == 2):
        transferKeuangan()

    elif (hasilInput == 3):
        informasiSaldo()
        pause()

    elif (hasilInput == 0):
        print("        Selesai, Terima Kasih!")
        break

    else:
        print("        Input tidak valid!")
        pause()

