# ==============================================================================
# Questão 2: Apresentar na tela os números ímpares no intervalo decrescente de 201 a 21.
# ==============================================================================

# Cabeçalho / Título da Saída
print("--- Números Ímpares no Intervalo de 201 a 21 (Decrescente) ---")

# Processamento e Saída de dados
# O comando range(201, 20, -2) inicia em 201, vai até 21 (parando antes do 20) 
# e decrementa de 2 em 2, garantindo que apenas os números ímpares sejam listados.
for i in range(201, 20, -2):
    print(i)