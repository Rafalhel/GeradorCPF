from random import randint
numero = str(randint(100000000,999999999))

novo_cpf = numero
x = 10
z = 0
try:
    for c in novo_cpf:
        c = int(c)
        y = c * x
        z += y
        result = 11 - (z % 11)
        if result > 10:
            result = 0
        x -= 1
        if x < 2:
            x = 11
    novo_cpf += str(result)
    y = 0
    z = 0
    for c in novo_cpf:
        c = int(c)
        y = c * x
        z += y
        result = 11-(z % 11)
        if result > 10:
            result=0
        x -= 1
    novo_cpf += str(result)
except:
    print("Valor inválido")
print(novo_cpf)