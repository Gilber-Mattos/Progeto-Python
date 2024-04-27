# G) Você está desenvolvendo um programa para determinar se três segmentos 
# podem formar um triângulo. Para isso, o programa precisa receber as medidas 
# dos três segmentos e compará-las entre si. A resposta resultante dessa comparação 
# deve indicar se os segmentos fornecidos podem formar um triângulo ou não.

import os


os.system('cls')

print('-'*70)
print('SAIBA SE TRÊS MEDIDAS FORMAM UM TRIANGULO.')
print('='*70)

# ENTRADA
a = float(input('Digite o 1º tamanho: '))
b = float(input('Digite o 2º tamanho: '))
c = float(input('Digite o 3º tamanho: '))

# Processamento
if (a + b > c and b + c > a and c + a >b):
    print(f'As medidas {a: .0f}, {b: .0f}, {c: .0f}')
    print('Podem Formar um triangulo.')
else:
    print('Não pode ser um triangulo')

print('.'*70)