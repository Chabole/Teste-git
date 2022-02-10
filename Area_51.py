
import numpy as np
import random

def sortear():
    return random.randint(1, 60)

#x = int(input('Quantos jogos serão jogados: '))

x = 3

lista = []
for _ in range(10):
    lista.append(sortear())

for jogo in range(x):
    print(f'-------- JOGO {jogo+1} --------')
    lista = []
    for i in range(6):
        lista.append(random.randint(0,60))
    print(f'{lista}')
    print('------------------------')