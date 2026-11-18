# ==============================================================================
# Questão 11: Maior valor bruto de vendas entre 35 vendedores (Loja "Pé vestido")
# ==============================================================================

print("=== APURAÇÃO DE VENDAS - LOJA PÉ VESTIDO ===")

# Inicialização das variáveis de controle
maior_venda = -1
nome_vendedor_campeao = ""

# Laço de repetição para os 35 vendedores
for i in range(1, 36):
    print(f"\n--- Vendedor {i} de 35 ---")
    nome = input("Digite o nome do vendedor: ")
    vendas = float(input("Digite o valor bruto das vendas: "))

    # Processamento: Verifica se bateu o recorde de vendas
    if vendas > maior_venda:
        maior_venda = vendas
        nome_vendedor_campeao = nome

# Saída de Dados (Resultado Final)
print("\n" + "=" * 55)
print("                  RESULTADO FINAL                  ")
print("=" * 55)
print(f"O vendedor com o maior valor bruto de vendas é: {nome_vendedor_campeao}")
print(f"Valor das vendas: R$ {maior_venda:.2f}")
print("=" * 55)