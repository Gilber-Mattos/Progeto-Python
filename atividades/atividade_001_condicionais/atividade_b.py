# B) A empresa "DataMax" está desenvolvendo um novo software de análise estatística 
# e precisa de uma funcionalidade que permita aos usuários inserir três números e, 
# em seguida, exibir na tela qual é o maior número, qual é o menor número ou se os 
# números são todos iguais. Essa funcionalidade é crucial para os analistas de dados 
# da "DataMax" que trabalham com conjuntos de dados diversos e precisam rapidamente 
# identificar as características básicas desses conjuntos, como a presença de outliers 
# ou a uniformidade dos números.

import os


os.system('cls')

print('-'*70)
print('ANÁLISE ESTATÍSTICA DE DADOS')
print('-'*70)

# Entrada
numero1 = float(input('Digite o 1º número: '))
numero2 = float(input('Digite o 2º número: '))
numero3 = float(input('Digite o 3º numero: '))
print('='*70)

# QUAL NÚMERO É O MAIOR
if (numero1 > numero2 and numero1 > numero3):
    print(f'{numero1: .0f} é o Maior')
    
elif (numero2 > numero1 and numero2 > numero3):
    print(f'{numero2: .0f} é o Maior')

else:
    print(f'{numero3: .0f} é o Maior')
    
print('-'*70)

# QUAL NÚMERO É O MENOR
if (numero1 < numero2 and numero1 < numero3):
    print(f'{numero1: .0f} é o Menor')
    
elif (numero2 < numero1 and numero2 < numero3):
    print(f'{numero2: .0f} é o Menor')

else:
    print(f'{numero3: .0f} é o Menor')
    
print('-'*70)

# OS NÚMEROS SÃO IGUAIS?
if (numero1 == numero2 == numero3):
    print('Os números são iguais! ')
else:
    print('Os números não são iguais! ')

print('-'*70)