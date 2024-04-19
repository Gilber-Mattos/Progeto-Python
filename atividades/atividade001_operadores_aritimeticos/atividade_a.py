# Faça um programa que peça 3 valores , depois calcule e imprima  a soma e a multiplicação desses valores. 

# Imports
import os


# Limpar o terminal
os.system('cls')

print('-'*70)
print('SOMA E MULTIPLICAÇÃO')
print('='*70)

# Entrada
valor1 = float(input('Digite o 1º número: '))
valor2 = float(input('Digite o 2º número: '))
valor3 = float(input('Digite o 3º número: '))

# Processamento
soma = valor1 + valor2 + valor3
multiplicacao = valor1 * valor2 * valor3

# Saída
print()
print('='*70)
print(f'A soma dos números é: {soma} ')
print(f'A multiplicação dos números é: {multiplicacao}')
print()
print('°'*70)