# Faça um programa que receba e divida 2 números. A saída da divisão precisará ser formatada com 4 casas decimais.

# Imports
import os


print('-'*70)
print('DIVISÃO DOS VALORES')
print('='*70)

# Entrada
dividendo = float(input('Digite o 1º número:'))
divisor = float(input('Digite o 2º Número: '))

# Processamento
divisao = dividendo / divisor

# Saída
print()
print('-'*70)
print(f'Resultado da divisão: {divisao: .4f}')