# Imports
# Biblioteca para interagir o SO
import os
# Biblioteca para pegar data e hora do sistema
import datetime


# limpar o terminal
os.system('cls')

print('-'*70)
print('ENTRE COM OS SEUS DADOS')
print('='*70)

# Entrada de dados com Casting
nome = str (input('Digite seu nome: '))
telefone = str (input('Digite seu telefone: '))
cpf = int (input('Digite seu CPF: '))
rua = str (input('Digite sua Rua: '))
bairro = str (input('Digite o bairro: '))
número =int (input('Digite o número da Residencia: '))

# Saída interpolada, utilizando o método type para
# verificar o tipo de variavel
print('='*70)
print(f'Bem vindo {nome}. ', type (nome))
print(f'Portador do CPF: {cpf}.', type (cpf))
print(f'Seu número de telefone: {telefone}.', type (telefone))
print(f'Seu endereço, {rua}, ', type (rua))
print(bairro , type (bairro))
print(f'Número da Residência: {número}. ', type (número))