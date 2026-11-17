# ==============================================================================
# Questão 3: Receber o preço de 10 produtos e mostrar a média de preços.
# ==============================================================================

# Inicialização do acumulador de preços
soma_precos = 0.0

print("--- Cálculo da Média de Preços de 10 Produtos ---")

# Entrada de dados e Processamento
for i in range(1, 11):
    # Lê o preço de cada um dos 10 produtos convertendo para número decimal (float)
    preco = float(input(f"Digite o preço do {i}º produto: R$ "))
    
    # Acumula o valor somando o preço atual ao total acumulado
    soma_precos += preco

# Cálculo final da média (soma total dividida pela quantidade de produtos)
media_precos = soma_precos / 10

# Saída de dados
print("-" * 45)
print(f"A média de preços dos 10 produtos é: R$ {media_precos:.2f}")
print("=" * 45)