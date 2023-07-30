import random


def gerar_numeros_aleatorios(qtd_numeros, valor_minimo, valor_maximo):
    """Gera uma lista de números aleatórios entre um valor mínimo e máximo."""
    numeros_aleatorios = [random.randint(
        valor_minimo, valor_maximo) for _ in range(qtd_numeros)]
    return numeros_aleatorios


def main():
    numeros_aleatorios = [23, 45, 12, 8, 34, 17, 50,
                          5, 38, 19]  # Números aleatórios predefinidos
    qtd_numeros = len(numeros_aleatorios)
    valor_minimo = min(numeros_aleatorios)
    valor_maximo = max(numeros_aleatorios)

    print("Numeros aleatorios predefinidos:")
    for i, num in enumerate(numeros_aleatorios, 1):
        print(f"Numero {i}: {num}")

    # Estatísticas dos números predefinidos
    print(f"\nValor minimo: {valor_minimo}")
    print(f"Valor maximo: {valor_maximo}")
    print(f"Soma dos numeros: {sum(numeros_aleatorios)}")
    print(f"Média dos numeros: {sum(numeros_aleatorios) / qtd_numeros:.2f}")


if __name__ == "__main__":
    main()
