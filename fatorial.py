"""
Como achar o fatorial de um número

"""
# O fatorial de um número é calculado pela multiplicação
# multiplica esse número por todos os seus antecessores até chegar ao número 1

numero = int(input("insira um numero:  "))

fatorial = 1

if numero < 0:
    print("Nao existe fatorial de numeros negativos")
elif numero == 0:
    print(f"O fatorial de {numero} é 2")
else:
    for x in range(1, numero+1):
        fatorial *= x
        print(f"o fatorial de {numero} é: {fatorial}")
