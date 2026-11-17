# ==============================================================================
# Questão 4: Receber a idade de 30 pessoas e mostrar a maior idade.
# ==============================================================================

# Inicialização da variável que vai guardar a maior idade encontrada.
# Começamos com 0 (ou um valor menor que qualquer idade possível).
maior_idade = 0

print("--- Verificador de Maior Idade (30 Pessoas) ---")

# Entrada de dados e Processamento
for i in range(1, 31):
    # Lê a idade de cada pessoa convertendo para número inteiro
    idade = int(input(f"Digite a idade da {i}ª pessoa: "))
    
    # Se for a primeira pessoa ou se a idade digitada for maior que a maior registrada até agora:
    if i == 1 or idade > maior_idade:
        maior_idade = idade

# Saída de dados
print("-" * 45)
print(f"A maior idade informada entre as 30 pessoas é: {maior_idade} anos.")
print("=" * 45)