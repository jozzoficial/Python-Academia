class GrafoPonderado:

    def __init__(self):
        self.adjacencia = {}

    def adicionar_no(self, no): #aqui nós começamos por criar o grafo
        if no not in self.adjacencia: #nó adjacente
            self.adjacencia[no] = []

    def adicionar_aresta(self, origem, destino, peso): # Aqui começamos por adicionar as arestas
        #E em relação aos nós, caso não existirem serão criados automaticamente
        if peso < 0: #Como o algoritmo de Dijkstra não suporta valores negativos, este passo serve para verificar e informar
            raise ValueError(
                f"Peso negativo ({peso}) não é suportado pelo algoritmo de Dijkstra."
            )

        self.adicionar_no(origem) #Adiciona o nó de origem
        self.adicionar_no(destino) #Adiciona o nó de destino
        self.adjacencia[origem].append((destino, peso)) #Estabelece o peso entre as arestas
        self.adjacencia[destino].append((origem, peso)) # Aqui também é estabelecido o peso na aresta

# Aqui fazemos a validação da criação do nosso grafo

    def no_existe(self, no): #Aqui procuramos verificar se o nó existe no grafo criado
        return no in self.adjacencia

    def nos(self): #Aqui fazemos o retorno, listando os elementos do nosso grafo
        return list(self.adjacencia.keys())

    def total_nos(self): # Aqui procuramos mostrar o número de nós que existem no nosso grafo
        return len(self.adjacencia)

    def total_arestas(self): # Procuramos ser claros, mostrando também o número de arestas que tem o nosso grafo
        return sum(len(v) for v in self.adjacencia.values()) // 2

# Aqui fazemos a exibição do grafo

    def exibir(self): # Aqui imprimimos a lista dos componentes do grafo de maneira formatada
        print("\nLista de Adjacência do Grafo")
        print(" " * 48)
        for no, vizinhos in self.adjacencia.items():
            if vizinhos:
                ligacoes = ",  ".join(f"{v} ({p} km)" for v, p in vizinhos)
            else:
                ligacoes = "(nó isolado)"
            print(f"  {no:12} →  {ligacoes}")
        print(f"\n  Nós: {self.total_nos()}   |   Arestas: {self.total_arestas()}")
        print(" " * 48)
