"""
def reduzirNumero(numeroInt):
    print(numeroInt)
    if numeroInt > 0:
        reduzirNumero(numeroInt - 1)

        reduzirNumero(5)

"""

"""

# Fatorial sem recursão

def fatorialS(numero):
    fatorial = 1
    if numero == 0:
        return 1
    else:
        for x in range(1, numero + 1):
            fatorial *= x
            return fatorial

        print(fatorialS(12))

"""

# Fatorial - Solução Recursiva


def fatorialR(numero):
    if numero == 0:
        return 1
    else:
        return numero * fatorialR(numero - 1)


print(fatorialR(5))
