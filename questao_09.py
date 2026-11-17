# ==============================================================================
# Questão 9: Receber 30 números e mostrar o maior e o segundo maior número.
# ==============================================================================

print("=== ENCONTRAR O MAIOR E O SEGUNDO MAIOR NÚMERO (30 NÚMEROS) ===")

# Entrada do primeiro número para servir de base inicial
numero = float(input("Digite o primeiro número: "))
maior = numero
segundo_maior = numero

# Laço de repetição para os 29 números restantes
for i in range(2, 31):
    numero = float(input(f"Digite o {i}º número: "))
    
    # Processamento lógico
    if numero > maior:
        segundo_maior = maior
        maior = numero
    elif numero > segundo_maior and numero != maior:
        segundo_maior = numero

# Saída de dados (Resultados Finais)
print("\n" + "=" * 45)
print("             RESULTADO FINAL             ")
print("=" * 45)
print(f"O maior número é:         {maior}")
print(f"O segundo maior número é: {segundo_maior}")
print("=" * 45)