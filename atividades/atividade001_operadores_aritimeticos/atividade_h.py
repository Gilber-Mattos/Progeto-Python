# Faça um programa que receba um número inteiro, depois imprima sua tabuada de multiplicação.

# Import
import os


# Limpar terminal
os.system('cls')

print('=')
print()
print('----------TABUADA----------')
print('='*70)

# Entrada
numero = int(input('Digite um número: '))

# Processamento
tabuada1 = numero * 0
tabuada2 = numero * 1
tabuada3 = numero * 2
tabuada4 = numero * 3
tabuada5 = numero * 4
tabuada6 = numero * 5
tabuada7 = numero * 6
tabuada8 = numero * 7
tabuada9 = numero * 8
tabuada10 = numero * 9

# Saída
print()
print('-'*70)
print(f'A tabuada de {numero} é: ')
print(f'{numero} x 0 = {tabuada1}')
print(f'{numero} x 1 = {tabuada2}')
print(f'{numero} x 2 = {tabuada3}')
print(f'{numero} x 3 = {tabuada4}')
print(f'{numero} x 4 = {tabuada5}')
print(f'{numero} x 5 = {tabuada6}')
print(f'{numero} x 6 = {tabuada7}')
print(f'{numero} x 7 = {tabuada8}')
print(f'{numero} x 8 = {tabuada9}')
print(f'{numero} x 9 = {tabuada10}')