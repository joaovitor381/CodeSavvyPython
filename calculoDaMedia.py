"""
O cálculo da média da nota do aluno;
Somando a nota1 e nota2;
Se a nota for igual ou maior que 7, estará aprovado.

"""


def ler_nota(aluno_num):
    while True:
        try:
            nota = float(input(f'Digite a nota {aluno_num} do aluno(a): '))
            return nota
        except ValueError:
            print("Valor inválido. Por favor, digite um número válido.")


def calcular_media(n1, n2):
    return (n1 + n2) / 2


def obter_resultado(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"


def main():
    nota1 = ler_nota("1")
    nota2 = ler_nota("2")
    media_aluno = calcular_media(nota1, nota2)

    print("\nNota 1:", nota1)
    print("Nota 2:", nota2)
    print("Média:", media_aluno)

    resultado_aluno = obter_resultado(media_aluno)
    print("Resultado:", resultado_aluno)


if __name__ == "__main__":
    main()
