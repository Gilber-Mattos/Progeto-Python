# Faça um programa que receba um número qualquer e calcule o dobro e o triplo desse número.

# Import
import os


os.system('cls')

print('-'*70)
print('calcule o dobro e o triplo do número')
print('-'*70)
print()

# Entrada
numero = float(input('Digite o Número desejado: '))

# Processamento
dobro = numero * 2
triplo = numero * 3

# Saida
print()
print('='*70)
print(f'O dobro de {numero} é: {dobro}')
print(f'O triplo de {numero} é: {triplo}')
print('='*70)