# D) A empresa "SalaryBoost" está implementando um sistema automatizado 
# para calcular os aumentos salariais de seus funcionários com base em 
# critérios específicos. Eles precisam de um programa que receba como 
# entrada o salário atual de um funcionário e, em seguida, calcule o novo 
# salário com base em determinadas condições. Essas condições incluem um 
# aumento de 5% caso o salário atual seja superior a R$1500,00, e um aumento 
# de 10% caso o salário atual seja inferior a R$1000,00. Além disso, o 
# programa deve garantir que o salário informado não seja igual a zero ou 
# negativo, pois isso não seria válido.

import os


os.system('cls')

print('-'*70)
print('SAIBA O SEU AUMENTO SALARIAL.')
print('='*70)

# ENTRADA
salario = float(input('Qual o seu Salário? '))
print('='*70)

# CONDIÇÃO
if salario >= 1500:
    salario1500 = salario * (5 / 100)
    salario_atual1 = salario + salario1500
    print(f'Seu novo salário é {salario_atual1}')
    
elif (salario > 0 and salario < 1499):
    salario1000 = salario * (10 / 100)
    salario_atual2 = salario + salario1000
    print(f'Seu novo salário é {salario_atual2}')
    
else:
    print(f'Salário {salario} inválido')    