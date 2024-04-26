# Faça um programa que converta metros em centímetros e milímetros.

# Import
import os


# Limpar terminal
os.system('cls')

print('-'*70)
print('CONVERTA METROS EM CENTÍMETROS E MILÍMETROS')
print('='*70)

# Entrada
metros = float(input('Digite a Metragem que deseja converter: '))

# Processamento
centimetro = metros * 100
milimetro = metros * 1000

# Saída
print()
print('='*70)
print(f'A metragem de {metros} é igual a: {centimetro}cm, e {milimetro}mil. ')