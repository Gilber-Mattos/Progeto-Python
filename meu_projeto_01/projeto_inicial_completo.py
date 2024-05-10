# Nome do Projeto a ser definido
# Autor: Gilber Mattos Mendes
# Data Inicial: 25/04/2024

import os
import random
import math


os.system('cls')

print('-'*70)
print('GERE UM NÚMERO ALEATÓRIO E DESCUBRA SE É PAR OU IMPAR')
print('-'*70)

print('Número inteiro aleatório: ')
numero_aleatorio = random.randint(1, 100)
print(f'Número gerado: {numero_aleatorio}')

# ENTRADA
decisao = input('Deseja gerar outro número? (SIM) (NÃO)')

# CONDIÇÃO / PROCESSAMENTO
if decisao == 'sim' or 'SIM':
    print('Número inteiro aleatório: ')
    numero_aleatorio2 = random.randint(1, 100)
    print(f'Número gerado: {numero_aleatorio}')
    
    escolha = input('Escolhha uma opção:'
          'a)SOMA'
          'b)DIVISÃO'
          'c)MULTIPLICAÇÃO'
          'd)SUBTRAÇÃO')
    if escolha == 'a':
        print('SOMA')
        soma = numero_aleatorio + numero_aleatorio2
    else:
        print(f'{numero_aleatorio} é IMPAR.') 
else:
    print('Fim do Programa')
    print('-'*70)