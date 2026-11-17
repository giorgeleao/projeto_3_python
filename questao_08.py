# ==============================================================================
# Questão 8: Receber o salário e o cargo de 30 funcionários e mostrar a 
# média de salários por cargo (Analista ou Técnico).
# ==============================================================================

# Inicialização dos acumuladores de salários e contadores de funcionários
soma_salario_analista = 0.0
soma_salario_tecnico = 0.0
qtd_analistas = 0
qtd_tecnicos = 0

print("=== CÁLCULO DE MÉDIA SALARIAL POR CARGO (30 FUNCIONÁRIOS) ===")

# Laço de repetição para os 30 funcionários
for i in range(1, 31):
    print(f"\n--- Funcionário {i} de 30 ---")
    salario = float(input("Digite o salário do funcionário: R$ "))
    # .strip().lower() garante que mesmo se digitar com letra maiúscula vai funcionar
    cargo = input("Digite o cargo do funcionário (analista/tecnico): ").strip().lower()
    
    # Processamento condicional por cargo
    if cargo == "analista":
        soma_salario_analista += salario
        qtd_analistas += 1
    else:
        soma_salario_tecnico += salario
        qtd_tecnicos += 1

# Cálculo das médias (com proteção matemática básica para evitar divisão por zero)
media_analista = soma_salario_analista / qtd_analistas if qtd_analistas > 0 else 0
media_tecnico = soma_salario_tecnico / qtd_tecnicos if qtd_tecnicos > 0 else 0

# Saída de dados (Resultados Finais formatados com 2 casas decimais)
print("\n" + "=" * 50)
print("                RESULTADO FINAL                ")
print("=" * 50)
print(f"Média salarial dos Analistas: R$ {media_analista:.2f}")
print(f"Média salarial dos Técnicos:  R$ {media_tecnico:.2f}")
print("=" * 50)