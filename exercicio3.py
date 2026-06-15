#Problema: Implemente uma função para detetar se um grafo direcionado contém um ciclo,
#utilizando Busca em Profundidade (DFS).

class GrafoCiclo:
    def __init__(self):
        self._adjacencia = {}

    def adicionar_aresta(self, u, v):
        if u not in self._adjacencia:
            self._adjacencia[u] = []

        if v not in self._adjacencia:
            self._adjacencia[v] = []

        self._adjacencia[u].append(v)

    def _dfs_detectar_ciclo(self, vertice, visitados, pilha_recursao):
        visitados.add(vertice)
        pilha_recursao.add(vertice)

        for vizinho in self._adjacencia.get(vertice, []):
            if vizinho not in visitados:
                if self._dfs_detectar_ciclo(vizinho, visitados, pilha_recursao):
                    return True

            elif vizinho in pilha_recursao:
                # Vizinho já está na pilha de recursão = ciclo!
                return True

        # Remover do caminho atual da recursão
        pilha_recursao.remove(vertice)

        return False

    def contem_ciclo(self):
        visitados = set()       # Nós visitados globalmente
        pilha_recursao = set()  # Nós no caminho da recursão atual

        for vertice in self._adjacencia:
            if vertice not in visitados:
                if self._dfs_detectar_ciclo(
                    vertice,
                    visitados,
                    pilha_recursao
                ):
                    return True

        return False


# Exemplo de uso
g_sem_ciclo = GrafoCiclo()

g_sem_ciclo.adicionar_aresta("A", "B")
g_sem_ciclo.adicionar_aresta("B", "C")
g_sem_ciclo.adicionar_aresta("C", "D")

print("\n--- Detecção de Ciclo em Grafo Direcionado ---")
print(f"Grafo sem ciclo: {g_sem_ciclo.contem_ciclo()}")  # False


g_com_ciclo = GrafoCiclo()

g_com_ciclo.adicionar_aresta("A", "B")
g_com_ciclo.adicionar_aresta("B", "C")
g_com_ciclo.adicionar_aresta("C", "A")  # Ciclo A -> B -> C -> A

print(f"Grafo com ciclo: {g_com_ciclo.contem_ciclo()}")  # True


g_complexo = GrafoCiclo()

g_complexo.adicionar_aresta("0", "1")
g_complexo.adicionar_aresta("0", "2")
g_complexo.adicionar_aresta("1", "2")
g_complexo.adicionar_aresta("2", "0")  # Ciclo
g_complexo.adicionar_aresta("2", "3")
g_complexo.adicionar_aresta("3", "3")  # Auto-ciclo

print(f"Grafo complexo com ciclo: {g_complexo.contem_ciclo()}")  # True