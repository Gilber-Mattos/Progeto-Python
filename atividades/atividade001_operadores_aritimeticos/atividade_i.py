# Faça um programa que receba um valor em reais, depois calcule quantos dólares daria para comprar com esse valor.

# Import
import os


print('-'*70)
print('TRANSFORME REAL EM DOLAR')
print('='*70)

# Entrada
real = float(input('Digite o valor em Real: '))

# Processamento
dolar = real * 5.20

# Saída
print()
print('-'*70)
print(f'{real} = {dolar} Dolar')