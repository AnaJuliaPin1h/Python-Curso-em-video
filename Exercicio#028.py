# Jogo da Adivinhação v.1.0

from random import randint
from time import sleep
pc = randint(0,5) 
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-" * 20)

j = int(input("Em que numero eu pensei? "))
print("PROCESSANDO.....")
sleep(3)
if j == pc:
    print("PARABÉNS! Você conseguiu me vencer! ")
else: 
    print("GANHEI! Eu pensei no numero {} e não no {}!" .format(pc,j))