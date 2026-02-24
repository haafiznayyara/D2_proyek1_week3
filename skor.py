from data import *

# Fungsi untuk menghitung skor berdasarkan jawaban pemain 
def hitung_skor(user_answer, i, score):
    if user_answer == quiz_data[i]['answer']:
        score += 100 / len(quiz_data)
    else:
        score += 0
    
    print(f"Skor Anda saat ini: {score}")
    return score