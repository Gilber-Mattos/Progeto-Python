# Faça um programa que receba um número inteiro e mostre o sucessor e antecessor.

# Import
import os


# Limpar Terminal
os.system('cls')

print('DESCUBRA O SUCESSOR E ANTECESSOR DE UM NÚMERO.')
print('='*70)
print()

# Entrada
inteiro = int(input('Digite um número: '))

# Processamento
antecessor = inteiro - 1
sucessor = inteiro + 1

# Saída
print()
print('+'*70)
print(f'O atecessor de {inteiro} é: {antecessor}.')
print(f'O sucessor de {inteiro} é: {sucessor}.')