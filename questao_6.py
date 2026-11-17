# ==============================================================================
# Questão 6: Pesquisa de votos para o nome do time do clube "Bela Vida"
# Baseado no fluxograma com 200 torcedores e contagem de votos/nulos.
# ==============================================================================

# Declaração e inicialização dos contadores de votos
votos1 = 0
votos2 = 0
votos3 = 0
votos4 = 0
votosNulos = 0

print("=== VOTAÇÃO: NOME DO TIME DO CLUBE 'BELA VIDA' ===")
print("Opções:")
print("1 - Perebas")
print("2 - Pernetas")
print("3 - Sonhadores")
print("4 - Perdidos")
print("================================================")

# Laço de repetição para os 200 torcedores
for i in range(1, 201):
    # Entrada de dados (lê o voto de cada torcedor)
    voto = int(input(f"Torcedor {i}º - Digite o voto (1 a 4): "))
    
    # Processamento / Estrutura de Decisão em Cascata
    if voto == 1:
        votos1 += 1
    else:
        if voto == 2:
            votos2 += 1
        else:
            if voto == 3:
                votos3 += 1
            else:
                if voto == 4:
                    votos4 += 1
                else:
                    # Qualquer valor diferente de 1 a 4 é contabilizado como nulo
                    votosNulos += 1

# Saída de dados (Resultados Finais)
print("\n" + "=" * 45)
print("          RESULTADO FINAL DA PESQUISA          ")
print("=" * 45)
print(f"Total de votos para Perebas (1):    {votos1}")
print(f"Total de votos para Pernetas (2):   {votos2}")
print(f"Total de votos para Sonhadores (3): {votos3}")
print(f"Total de votos para Perdidos (4):   {votos4}")
print(f"Total de votos nulos:               {votosNulos}")
print("=" * 45)