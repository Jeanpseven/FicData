from faker import Faker
import random

fake = Faker()

# Lista de nacionalidades disponíveis
nacionalidades = ["pt_BR", "en_US", "es_ES", "fr_FR"]

# Pedir ao usuário para escolher uma nacionalidade
print("Escolha uma nacionalidade disponível:")
for i, nacionalidade in enumerate(nacionalidades, 1):
    print(f"{i}. {nacionalidade}")
print("Digite o número correspondente à nacionalidade desejada ou 'list' para ver a lista:")

while True:
    escolha = input()
    if escolha == 'list':
        for i, nacionalidade in enumerate(nacionalidades, 1):
            print(f"{i}. {nacionalidade}")
        print("Digite o número correspondente à nacionalidade desejada:")
    elif escolha.isnumeric():
        escolha = int(escolha)
        if 1 <= escolha <= len(nacionalidades):
            nacionalidade_escolhida = nacionalidades[escolha - 1]
            break
        else:
            print("Número fora do intervalo. Digite um número válido.")
    else:
        print("Entrada inválida. Digite 'list' ou o número correspondente à nacionalidade.")

# Resto do seu código
fake = Faker(nacionalidade_escolhida)

# Agora você pode continuar com o restante do seu código usando a nacionalidade escolhida