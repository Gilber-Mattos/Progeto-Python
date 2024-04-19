# Faça um programa que peça o ano do seu nascimento e calcule a sua idade.

# Imports
import os
import datetime


# Limpar o terminal
os.system('cls')

print('-'*70)
print('DESCUBRA A SUA IDADE')
print('-'*70)
print()

# Entrada
ano_nascimento = int(input('Qual ano você nasceu? '))

# Processamento
ano_atual = datetime.datetime.now().year
idade = ano_atual - ano_nascimento

# Saída
print()
print('+'*70)
print()
print(f'Sua idade é: {idade}.')
print('~'*70)
