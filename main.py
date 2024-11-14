def gerar_treino(biotipo, tempo_disponivel, preferencia_exercicio):
    treino = f"Treino ideal para o biotipo {biotipo}, com {tempo_disponivel} minutos de disponibilidade e foco em {preferencia_exercicio}."
    return treino

# Exemplo de entrada para teste
if __name__ == "__main__":
    biotipo = input("Informe seu biotipo (ectomorfo, mesomorfo, endomorfo): ")
    tempo_disponivel = input("Informe o tempo disponível para o treino (em minutos): ")
    preferencia_exercicio = input("Informe seu tipo de exercício preferido (cardio, força, flexibilidade): ")

    print(gerar_treino(biotipo, tempo_disponivel, preferencia_exercicio))
