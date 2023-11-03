from faker import Faker
import random

fake = Faker()

# Pedir ao usuário a idade mínima e máxima desejada
idade_minima = int(input("Digite a idade mínima desejada: "))
idade_maxima = int(input("Digite a idade máxima desejada: "))

# Pedir ao usuário o número de dados a serem gerados
quantidade_dados = int(input("Digite o número de dados a serem gerados: "))

# Inicializar uma lista para armazenar os dados gerados
log = []

# Gerar os dados solicitados e armazená-los na lista
for _ in range(quantidade_dados):
    nome_ficticio = fake.name()
    idade_aleatoria = random.randint(idade_minima, idade_maxima)
    numero_telefone_ficticio = fake.random_int(31000000000, 31999999999)
    
    # Adicionar os dados à lista
    log.append({
        "Nome": nome_ficticio,
        "Idade": idade_aleatoria,
        "Número de Telefone": numero_telefone_ficticio
    })

# Imprimir os dados gerados
for dados in log:
    print(f"Nome: {dados['Nome']}")
    print(f"Idade: {dados['Idade']} anos")
    print(f"Número de Telefone: {dados['Número de Telefone']}")
    print("\n")
