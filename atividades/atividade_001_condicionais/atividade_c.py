# C) A empresa "SafeDrive" está desenvolvendo um sistema de monitoramento de velocidade
# para ajudar a promover a segurança nas estradas. Eles precisam de um programa que 
# permita aos usuários inserir a velocidade de um carro e, em seguida, exibir na tela 
# uma mensagem adequada com base na velocidade fornecida. O objetivo principal é alertar 
# os motoristas caso ultrapassem o limite de velocidade de 60 km/h, incentivando-os a 
# dirigir dentro dos limites legais e, assim, reduzir o risco de acidentes.

import os


os.system('cls')

print('-'*70)
print('RADAR 60 KM/h')
print('='*70)

# Entrada
velocidade = float(input('Digite os KM /h que o veículo estava: '))
print('-'*70)

# CONDIÇÃO
if velocidade > 60:
    print(f'O veículo ultrapassou a velocidade permitida')
    print(f'estava a {velocidade: .0f} km /h.')
         
else:
    print('O veículo está dentro da velocidade permitida.')
    
print('.'*70)