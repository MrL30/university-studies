# Exercise 4: Check the conditions before executing the code

a = 8

if a > 10:
    print("a é maior que 10")
else:
    print("a é menor ou igual a 10")

# A: a é menor ou igual a 10
"""
============================================================
"""

x = 5
y = 12

if x < 10 and y > 10:
    print("Ambas as condições são verdadeiras")
else:
    print("Pelo menos uma condição é falsa")

# A: Ambas as condições são verdadeiras
"""
============================================================
"""

idade = 20
estudante = False

if idade < 18 or estudante:
    print("Tem acesso ao desconto")
else:
    print("Sem desconto")

# A: Sem desconto
"""
============================================================
"""

nota = 85

if nota >= 50:
    if nota >= 80:
        print("Excelente!")
    else:
        print("Passou")
else:
    print("Reprovou")

# A: Excelente!
"""
============================================================
"""

temperatura = 25

if temperatura > 30:
    print("Está muito quente")
elif temperatura > 20:
    print("Está agradável")
else:
    print("Está frio")

# A: Está agradável
"""
============================================================
"""

a = 10
b = 20

if a == 10 and not (b == 10):
    print("Condição cumprida")
else:
    print("Condição não cumprida")

# A: Condição cumprida
"""
============================================================
"""

flag = False

if flag:
    print("Flag é verdadeiro")
else:
    print("Flag é falso")

# A: Flag é falso
"""
============================================================
"""

x = 7
y = 15
z = 20

if x > 5 and (y < 10 or z > 15):
    print("Condição complexa verdadeira")
else:
    print("Condição complexa falsa")

# A: Condição complexa verdadeira
"""
============================================================
"""



a = 7
b = 10

if a >= 10 and not b != a:
    print("A")
elif a == b or a <= b:
    print("B")
else:
    print("C")

# A: B