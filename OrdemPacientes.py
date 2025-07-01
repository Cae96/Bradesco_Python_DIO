# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

# TODO: Ordene por prioridade: urgente > idosos > demais:

urgente =[x for x in pacientes if x[2]=="urgente"]
normal = [x for x in pacientes if x[2]=="normal"]

normal.sort(key=lambda x:x[1])
ordem_pacientes = []

# TODO: Exiba a ordem de atendimento com título e vírgulas:

print(f"Ordem de Atendimento:{ordem_pacientes}")