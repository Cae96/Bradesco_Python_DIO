def processar_reservas():
    # Entrada dos quartos disponíveis
    quartos_disponiveis = set(map(int, input().split()))
    
    # Entrada das reservas solicitadas
    reservas_solicitadas = list(map(int, input().split()))

    # TODO: Crie o processamento das reservas:
    

    # TODO: Verifique se cada reserva pode ser confirmada com base na disponibilidade dos quartos: 
    confirmadas = [x in x for reservas_solicitadas in quartos_disponiveis]
    recusadas = set(reservas_solicitadas) - quartos_disponiveis

    # Saída dos resultados conforme especificação
    print("Reservas confirmadas:", " ".join(map(str, confirmadas)))
    print("Reservas recusadas:", " ".join(map(str, recusadas)))

# Chamada da função principal
processar_reservas()