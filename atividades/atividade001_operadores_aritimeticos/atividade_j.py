# Faça um programa com entrada de dados para calcular o perímetro de um retângulo

#import
import os


# Limpar terminal
os.system('cls')

print('-'*70)
print('PERIMETRO DE UM RETANGULO')
print('-'*70)

# Entrada
base = float(input('Digite a base do retangulo: '))
altura = float(input('Digite a altura do retangulo: '))

# Processamento
perimetro = 2 * (base + altura)

# Saída
print()
print('-'*70)
print(f'O perímetro do retangulo é: {perimetro}.')
print('='*70)
