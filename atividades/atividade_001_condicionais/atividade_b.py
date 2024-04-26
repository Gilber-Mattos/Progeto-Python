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