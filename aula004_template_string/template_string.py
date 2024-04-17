# imports
# Biblioteca para interagir o SO
import os
# Biblioteca para pegar data e hora do sistema
import datetime


# limpar o terminal
os.system('cls')

print('-'*70)
print('ENTRADA DE DADOS EM PYTHON')
print('='*70)

# Entrada
nome = input('Entre com um nome: ')
peso = input('Entre com o peso: ')
altura = input('Entre com a altura: ')

# Entrada com Casting
nascimento = int(input('Data de nascimento: '))
cep = int(input('Entre com o seu CEP: '))
bairro = str(input('Entre com o Bairro: '))
rua = str(input('Nome da Rua: '))
numero = int(input('Entre com o número: '))

# Processamento: pegando o ano corrente
ano_atual = datetime.datetime.now().year
idade = int(ano_atual) - nascimento

# Saída
print('-'*70)
print('SAÍDA DE DADOS')
print('='*70)
print('Nome..............: ', nome)
print('Data de nascimento: ', nascimento)
print('Peso..............: ', peso)
print('Altura............: ', altura)

# Saída imterpolada
print(f'{nome}, você tem {idade} anos!')
print(f'Cep..............: {cep}')
print(f'Bairro...........: {bairro}')
print(f'rua..............: {rua}')
print(f'Número...........: {numero} ')
print('-'*70)
print('')
