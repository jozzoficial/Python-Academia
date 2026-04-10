from grafo import GrafoPonderado
from dijkstra import exibir_caminho, exibir_todas_distancias
#Definição do nosso grafo
def criar_grafo():
    """
    Criamos os nosso grafo com 7 nós (município do Uíge)

    Estrutura visual do grafo:

        Uíge ──37── Negage ──53── Puri
          |            |
          40           47
          |            |
        Bembe ──45── Bungo ──50── Milunga ──47── Songo
          |
          37
          |
        Songo

    Arestas e pesos (distâncias em km):
        Uíge   — Negage  :  37 km
        Negage — Puri    :  53 km
        Uíge   — Bembe   :  40 km
        Negage — Bungo   :  47 km
        Bembe  — Bungo   :  45 km
        Bungo  — Milunga :  50 km
        Milunga— Songo   :  47 km
        Bembe  — Songo   :  37 km
    """
    g = GrafoPonderado()

    g.adicionar_aresta("Uíge",    "Negage",   37)
    g.adicionar_aresta("Negage",  "Puri",     53)
    g.adicionar_aresta("Uíge",    "Bembe",    40)
    g.adicionar_aresta("Negage",  "Bungo",    47)
    g.adicionar_aresta("Bembe",   "Bungo",    45)
    g.adicionar_aresta("Bungo",   "Milunga",  50)
    g.adicionar_aresta("Milunga", "Songo",    47)
    g.adicionar_aresta("Bembe",   "Songo",    37)

    return g


#Algo similar na linguagem C, aqui demos o início do nosso programa principal
def main():
    print()
    print("  " + "=" * 48)
    print("   OTIMIZAÇÃO DE ROTAS — ALGORITMO DE DIJKSTRA")
    print("=" * 42)

    grafo = criar_grafo() # Aqui criamos o grafo principal
    grafo.exibir() # Aqui exibimos a estrutura do grafo

# Zona Para testes

    exibir_caminho(grafo, "Uíge", "Songo")

if __name__ == "__main__":
    main()
