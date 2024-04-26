# A) A empresa "TechSolutions" contratou você para desenvolver um programa em Python
# que irá automatizar uma parte do seu sistema de processamento de dados. Eles precisam 
# de um programa que solicite ao usuário a entrada de um número inteiro e, em seguida, 
# verifique se esse número é par ou ímpar. Essa funcionalidade é essencial para o sistema 
# deles, pois eles processam grandes conjuntos de dados e precisam classificar os números 
# de forma eficiente para realizar cálculos específicos em cada tipo de número.

import os


os.system('cls')

print('-'*70)
print('DESCUBRA SE UM NÚMERO É PAR OU ÍMPAR.')
print('-'*70)

# Entrada
numero = float(input('Digite um número: '))

# Condição
if numero % 2 == 0:
    print(f'{numero: .0f} é PAR')
else:
    print(f'{numero: .0f} é ÍMPAR')

print('-'*70)
print()