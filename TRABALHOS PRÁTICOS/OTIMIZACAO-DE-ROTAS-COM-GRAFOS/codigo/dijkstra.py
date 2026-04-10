import heapq # Usando a lógica de complexidade de algoritmos, decidimos importar o módulo nativo que permite
             # trabalhar com prioridade em filas permitibdo encontrar os menores ou maiores elementos de uma coleção.

def dijkstra(grafo, origem): #Aqui começamos por implementar o algoritmos de Dijkstra

    if not grafo.no_existe(origem): #Aqui decidimos fazer a verificação da existência do nó no grafo
                                    #Algo similar com o BREAK, aqui caso for executado, o fluxo do progama é interrompido
        raise ValueError(f"Nó de origem '{origem}' não existe no grafo.")

    distancias = {no: float('inf') for no in grafo.adjacencia} #Aqui, pensamos em inicializar com valores bastante grandes
                                                               # ou seja, com infinito
    distancias[origem] = 0 # A distância da origem continua sendo zero
    predecessores = {no: None for no in grafo.adjacencia} # Aqui procuramos registar cada nó no caminho ótimo
    fila = [(0, origem)] # Aqui fica armazenado a distância entre os nós quando o algoritmo percorre os nós

    # Conjunto de nós já finalizados (distância mínima confirmada)
    visitados = set() #Aqui ficam armazenados os nós percorridos (apenas os do caminho ótimo)

    while fila:

        dist_atual, no_atual = heapq.heappop(fila)
        if no_atual in visitados: # Aqui fazemos os testes entre as distâncias, onde se já foi processado com a menor distância, ignora
            continue
        visitados.add(no_atual)
        for vizinho, peso in grafo.adjacencia[no_atual]: #Ignora as arestas dos nós vizinhos
            nova_dist = dist_atual + peso

            if nova_dist < distancias[vizinho]:
                distancias[vizinho] = nova_dist
                predecessores[vizinho] = no_atual
                heapq.heappush(fila, (nova_dist, vizinho))

    return distancias, predecessores

#Aqui é onde fazemos a renconstrunção dos caminhos percorridos
def reconstruir_caminho(predecessores, origem, destino):
    if destino not in predecessores: #Aqui verificamos de o destino existe no grafo criado
        return []

    caminho = []
    no_atual = destino

    while no_atual is not None:
        caminho.append(no_atual)
        no_atual = predecessores[no_atual]

    caminho.reverse()

    if caminho[0] != origem: #Aqui verificamos se o caminho não começa na origem, logo o destino é inalcançável
        return []

    return caminho

#Aqui criamos funções que nos irão permitir exibir
def exibir_caminho(grafo, origem, destino):
    """
    Calcula e exibe o caminho mais curto entre dois nós,
    tratando todos os casos especiais (nó inexistente, inalcançável).

    Parâmetros:
        grafo   — instância de GrafoPonderado
        origem  — nó de partida
        destino — nó de chegada
    """
    print(f"\nOrigem: {origem}  →  Destino: {destino}")
    print("─" * 42)

    if not grafo.no_existe(origem): # Antes de calcular os nós, verificamos se eles existem
        print(f"Erro: o nó '{origem}' não existe no grafo.")
        print("─" * 42)
        return

    if not grafo.no_existe(destino):
        print(f"Erro: o nó '{destino}' não existe no grafo.")
        print("─" * 42)
        return

    if origem == destino:
        print(f"Origem e destino são o mesmo nó. Distância: 0 km.")
        print("─" * 48)
        return

    distancias, predecessores = dijkstra(grafo, origem)
    caminho = reconstruir_caminho(predecessores, origem, destino)

    if not caminho:
        print(f"Não existe caminho entre '{origem}' e '{destino}'.")
        print(f"(Nós não conectados no grafo.)")
    else:
        rota = " → ".join(caminho)
        total = distancias[destino]
        print(f"  Caminho   : {rota}")
        print(f"  Distância : {total} km")

    print("─" * 42)


def exibir_todas_distancias(grafo, origem): #Aqui exibimos as distâncias

    if not grafo.no_existe(origem): # Auto explicativo, mas em síntese decidmos verificar a existência do nó no grafo
        print(f"\nNó '{origem}' não existe no grafo.")
        return

    distancias, _ = dijkstra(grafo, origem)

    print(f"\nDistâncias mínimas a partir de '{origem}'")
    print("─" * 42)

    for cidade, dist in sorted(distancias.items(), key=lambda x: x[1]): #Aqui decidimos organizar os elementos de forma ascendente
        if dist == float('inf'):
            print(f"  {cidade:14} :  inalcançável")
        else:
            barra = "█" * dist
            print(f"  {cidade:14} : {dist:3} km  {barra}")

    print("─" * 42)
