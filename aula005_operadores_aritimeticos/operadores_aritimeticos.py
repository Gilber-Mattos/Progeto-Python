# imports
import os


# limpar o terminal
os.system('cls')

print('-'*70)
print('OPERADORES ARITIMÉTICOS')
print('='*70)

# Entrada de Dados
print('--- SOMA')
print('+'*70)
parcela_1 = float(input('Entre com a 1ª parcela: '))
parcela_2 = float(input('Entre com a 2ª parcela: '))

print()
print('--- SUBTRAÇÃO')
print('-'*70)
minuendo = float(input('Entre com o minuendo: '))
subtraendo = float(input('Entre com a subtraendo: '))

print()
print('--- PRODUTO')
print('-'*70)
multiplicando = float(input('Entre com o multiplicando: '))
multiplicador = float(input('Entre com o multiplicador: '))

print()
print('--- DIVISÃO')
print('-'*70)
dividendo = float(input('Entre como dividendo: '))
divisor = float(input('Entre com o divisor: '))

print()
print('--- RAIZ QUADRADA')
print('-'*70)
numero = float(input('Entre com um número desejado: '))

# Processamento
soma = parcela_1 + parcela_2
diferanca = minuendo - subtraendo
produto = multiplicando * multiplicador
quociente = dividendo / divisor
raiz_quadrada = numero **0.5

# Saída
print('='*70)
print('RESULTADOS')
print('-'*70)
print(f'A soma de {parcela_1} + {parcela_2} é: {soma}')
print(f'A subtração de {minuendo} - {subtraendo} é: {diferanca}')
print(f'A multiplicação de {multiplicando} x {multiplicador} é: {produto}')
print(f'A diferença de {dividendo} / {divisor} é {quociente}')
print(f'A raiz quadrada de {numero} é: {raiz_quadrada}')

# Seguindo os passos anteriores, desenvolva o restante
# Acrescente a raiz quadrada e a raiz cúbica.
