notaA = float(input("Informe a primeira nota: 9 "))
notaB = float(input("Informe a segunda nota: 5  "))

# calcular media
mediafinal = (notaA + notaB) / 2

# verificação
if mediafinal >= 7.0:
    print("A Média: %.1f - Aprovado " % mediafinal)
else:
    print("A Média: %.1f - Reprovado " % mediafinal)
