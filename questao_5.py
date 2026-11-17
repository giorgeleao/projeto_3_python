# ==============================================================================
# Questão 5: Receber o nome e a idade de 30 pessoas e mostrar o nome da mais velha.
# ==============================================================================

# Inicialização das variáveis de controle
maior_idade = 0
nome_mais_velho = ""

print("--- Identificador da Pessoa Mais Velha (30 Pessoas) ---")

# Entrada de dados e Processamento
for i in range(1, 31):
    print(f"\n--- Pessoa {i} de 30 ---")
    nome = input("Digite o nome: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    
    # Se for a primeira pessoa ou se a idade atual for maior que a maior registrada:
    if i == 1 or idade > maior_idade:
        maior_idade = idade
        nome_mais_velho = nome

# Saída de dados
print("\n" + "=" * 45)
print(f"A pessoa mais velha é {nome_mais_velho}, com {maior_idade} anos.")
print("=" * 45)