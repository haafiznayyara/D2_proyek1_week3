from ui import *

from playQuiz import mulai_quiz

mainLagi = True

while mainLagi:
    show_menu()
    score =0
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        mulai_quiz(score)    
            
    elif pilihan == "2":
        program_selesai()
        
    else:
        os.system('cls')
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

    mainLagi = main_lagi()
    