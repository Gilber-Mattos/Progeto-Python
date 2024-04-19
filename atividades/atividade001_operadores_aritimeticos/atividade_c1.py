# Faça um programa que peça 4 notas, após a entrada de dados calcular a média das notas digitadas.

# Imports
import os


# Limpar o Teminal
os.system('cls')

print('-'*70)
print('Calcule a sua Média.')
print('-'*70)

# Entrada
nota1 = float(input('Digite a nota do 1º Bimestre: '))
nota2 = float(input('Digite a nota do 2º Bimestre: '))
nota3 = float(input('Digite a nota do 3º Bimestre: '))
nota4 = float(input('Digite a nota do 4º Bimestre: '))

# Processamento
media = (nota1 + nota2 + nota3 + nota4) / 4

# Saída
print('-'*70)
print(f'Sua média é: {media}.')
print('='*70)