# ==============================================================================
# Questão 7: Receber o sexo de 200 pessoas e mostrar a quantidade 
# de homens e mulheres.
# ==============================================================================

# Inicialização dos contadores
qtd_homens = 0
qtd_mulheres = 0

print("=== CONTAGEM DE GÊNERO DE 200 PESSOAS ===")
print("Instruções: Digite 'M' para Masculino ou 'F' para Feminino.")
print("==========================================")

# Laço de repetição para as 200 pessoas
for i in range(1, 201):
    # Recebe o sexo, remove espaços em branco e converte para minúscula para facilitar a validação
    sexo = input(f"Pessoa {i} - Digite o sexo (M/F): ").strip().lower()
    
    # Processamento e contagem
    if sexo == 'm':
        qtd_homens += 1
    elif sexo == 'f':
        qtd_mulheres += 1
    else:
        print("Opção inválida! Digite apenas M ou F para esta pessoa.")
        # Opcional: Se quiser que a repetição peça novamente caso digitem errado, 
        # poderíamos usar um laço 'enquanto', mas mantendo o fluxo simples:

# Saída de dados (Resultados Finais)
print("\n" + "=" * 45)
print("             RESULTADO FINAL             ")
print("=" * 45)
print(f"Total de Homens:    {qtd_homens}")
print(f"Total de Mulheres:  {qtd_mulheres}")
print("=" * 45)