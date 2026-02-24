import os

from data import *
from skor import hitung_skor 

def mulai_quiz(score):
    for i in range (len(quiz_data)):
        os.system('cls')
        print(  f"{quiz_data[i]['q']}")
        
        for j in range(len(quiz_data[i]['options'])):
            print(f"{j+1}. {quiz_data[i]['options'][j]}")
            
        user_answer = int(input("Jawaban Anda (1-4): "))
        score = hitung_skor(user_answer, i, score)