# Importando a biblioteca de sistema
import os


# Limpando o terminal
os.system('cls')

print('-'*70) # firula
print('Estudo de variáveis')
print('='*70) # firula

# As variáveis são declaradas por inferência
nome = 'John Doe'
nascimento = 1970
altura = 1.80
peso = 75.5
doador = True
complexo = 3j  # Python trabalha diferente com números complexos
PI = 3.14  # isso é uma CONSTANTE, seu valor não deve ser alterado

# Saída utilizando o método type() para verificar o
# tipo da variável
print('\033[0m \033[31mTipos declarados:\033[0m')
print('\033[0m A var \033[32m nome \033[0m é do tipo: ', type(nome))
print('\033[0m A var \033[32m nascimento \033[om é do tipo: ', type(nascimento))
print('\033[0m A var \033[32m altura \033[0m é do tipo: ', type(altura))
print('\033[0m A var \033[32m peso \033[0m é do tipo ', type(peso))
print('\033[0m A var \033[32m doador \033[0m é do tipo:? ', type(doador))
print('\033[0m A var \033[32m complexo \033[0m é do tipo: ', type(complexo))
print('\033[0m A var \033[32m PI \033[0mé do tipo: ', type(PI))
print('-'*70)
print('')
