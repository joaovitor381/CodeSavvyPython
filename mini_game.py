from random import choice

jogador_vitorias = 0
maq_vitorias = 0


def Opcao_Jogador():
    valid_options = ["pedra", "papel", "tesoura"]
    while True:
        esc_jogador = input("Escolha Pedra, Papel ou Tesoura: ").lower()
        if esc_jogador in valid_options:
            return esc_jogador
        else:
            print("Opção inválida. Tente novamente")


def Opcao_Maquina():
    esc_maquina = choice(["pedra", "papel", "tesoura"])
    return esc_maquina


while True:
    print("-" * 30)
    esc_jogador = Opcao_Jogador()
    esc_maquina = Opcao_Maquina()
    print("-" * 30)

    if (esc_jogador == "pedra" and esc_maquina == "tesoura") or \
            (esc_jogador == "papel" and esc_maquina == "pedra") or \
            (esc_jogador == "tesoura" and esc_maquina == "papel"):
        # Jogador ganha
        print(f"Jogador escolheu {esc_jogador} Máquina escolheu {esc_maquina}"
              " Resultado: Você ganhou!")
        jogador_vitorias += 1
    elif esc_jogador == esc_maquina:
        # Empate
        print(f"Jogador escolheu {esc_jogador} Máquina escolheu {esc_maquina}"
              " Resultado: Empate")
    else:
        # Máquina ganha
        print(f"Jogador escolheu {esc_jogador} Máquina escolheu {esc_maquina}"
              " Resultado: Você Perdeu")
        maq_vitorias += 1

    print("-" * 30)
    print(f"Vitórias do Jogador: {jogador_vitorias}")
    print(f"Vitórias da Máquina: {maq_vitorias}")
    print("-" * 30)

    esc_jogador = input("Você quer jogar novamente? ")
    if esc_jogador.lower() not in ["sim", "s", "SIM", "S"]:
        break
