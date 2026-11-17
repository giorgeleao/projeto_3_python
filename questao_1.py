# ==============================================================================
# Questão 1: Apresentar na tela os números pares no intervalo de 10 a 200.
# ==============================================================================

# Cabeçalho / Título da Saída
print("--- Números Pares no Intervalo de 10 a 200 ---")

# Processamento e Saída de dados
# O comando range(10, 201, 2) inicia em 10, vai até 200 (201 exclusivo) 
# saltando de 2 em 2, garantindo que apenas os números pares sejam percorridos.
for i in range(10, 201, 2):
    print(i)

# Alternativa utilizando estrutura de condição (caso prefira testar o resto da divisão):
# for i in range(10, 201):
#     if i % 2 == 0:
#         print(i)