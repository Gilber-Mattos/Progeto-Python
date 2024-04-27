#H) A empresa "RootCalc" está desenvolvendo um software de cálculo 
# de raízes de equações quadráticas para auxiliar engenheiros e cientistas
# em suas análises e projetos. Eles precisam de um programa que calcule as 
# raízes da equação quadrática 𝑥²−6𝑥+5 sem depender de funções ou métodos 
# predefinidos, utilizando apenas os conceitos e operações básicas aprendidos 
# até o momento. Essas raízes são conhecidas como 𝑥’ = 5 e 𝑥’’ = 1, e o programa 
# deve ser capaz de calcular essas raízes de forma precisa, seguindo os princípios 
# matemáticos fundamentais.

import os


os.system('cls')

print('-'*70)
print('Vamos calcular as raízes da equação quadrática 𝑥²−6𝑥+5')
print('-'*70)

# elementos da equação
a = 1
b = -6
c = 5

# Calcular o discriminante delta
delta = b**2 - 4*a*c

# Condição de existência das raízes
if delta >= 0:
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)
    print('Raízes de equação quadrática 𝑥²−6𝑥+5')
    print(f'𝑥’ = {x1}')
    print(f'𝑥’’ = {x2}')
    
else:
    print('Nao há raizes para essa equação!')
    
print('.'*70)