# F) A empresa "LeapYearCheck" está desenvolvendo um software de verificação 
# de anos bissextos para auxiliar usuários na identificação desses anos de 
# forma rápida e precisa. Eles precisam de um programa que permita aos usuários 
# inserir um ano e, em seguida, determine se esse ano é bissexto ou não, de 
# acordo com as regras estabelecidas pelo calendário gregoriano. Além disso, 
# é necessário realizar a validação de entrada de dados para garantir que o 
# ano inserido pelo usuário seja um valor válido, ou seja, um número inteiro positivo.

import os


os.system('cls')

print('-'*70)
print('DESCUBRA SE UM ANO É BISSEXTO.')
print('='*70)

# Entrada
ano = int(input('Digite um ano: '))
print('-'*70)

# Processamento
if ano % 100 != 0 and ano % 4 == 0:
    print(f'{ano} é um ano Bissexto.')
    
else:
    print(f'{ano} Não é um ano Bissexto')
    
print('.'*70)