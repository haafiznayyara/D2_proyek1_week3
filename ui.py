import os
from data import *


def show_menu():
    print("=== Quiz Ngawur ===")
    print("1. Mulai Quiz")
    print("2. Keluar   ")
    

def program_selesai():
    print("Kanarazu Katsu! Terima kasih sudah bermain.")
    
def main_lagi():
    pilihan = input("Apakah Anda ingin bermain lagi? (y/n): ")
    if pilihan.lower() == 'y':
        os.system('cls')
        # show_menu()
        return True
    elif pilihan.lower() == 'n':
        program_selesai()
    else:
        print("Pilihan tidak valid. Silakan pilih 'y' atau 'n'.")
        main_lagi()