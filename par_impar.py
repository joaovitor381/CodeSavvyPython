def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"


if __name__ == "__main__":
    # Entrada do número pelo usuário
    num = int(input("Digite um numero inteiro: "))

    # Verificação se é par ou ímpar
    resultado = verificar_par_impar(num)

    # Exibição do resultado
    print(f"O número {num} é {resultado}.")
