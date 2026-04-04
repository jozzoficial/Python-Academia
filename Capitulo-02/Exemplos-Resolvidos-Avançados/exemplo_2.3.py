# Exemplo 2.3: Geração de Relatórios Dinâmicos com Funções de Ordem Superior

dados_vendas = [
    {"produto": "Laptop", "categoria": "Eletrônicos", "quantidade": 10, "preco_unitario": 1200},
    {"produto": "Teclado", "categoria": "Acessórios",
     "quantidade": 50, "preco_unitario": 50},
    {"produto": "Mouse", "categoria": "Acessórios", "quantidade":
        75, "preco_unitario": 25},
    {"produto": "Monitor", "categoria": "Eletrônicos",
     "quantidade": 15, "preco_unitario": 300},
    {"produto": "Webcam", "categoria": "Acessórios",
     "quantidade": 30, "preco_unitario": 70},
]


def gerar_relatorio(vendas, filtro_fn=None, transformacao_fn=None):  # Aplicar filtro, se houver
    vendas_filtradas = list(filter(filtro_fn, vendas)) if filtro_fn else vendas

    # Aplicar transformação, se houver
    vendas_transformadas = list(map(transformacao_fn, vendas_filtradas)) if transformacao_fn else vendas_filtradas

    return vendas_transformadas


# Filtro para eletrônicos
filtro_eletronicos = lambda item: item["categoria"] == "Eletrônicos"

# Transformação para calcular o total de vendas por item
transformacao_total_vendas = lambda item: {"produto": item["produto"], "total_venda": item["quantidade"] * item["preco_unitario"] }

# Relatório de todos os itens
print("\n--- Relatório Completo ---")
relatorio_completo = gerar_relatorio(dados_vendas)
for item in relatorio_completo:
    print(item)

# Relatório de eletrônicos com total de vendas
print("\n--- Relatório de Eletrônicos (Total de Vendas) ---")
relatorio_eletronicos = gerar_relatorio(dados_vendas, filtro_fn = filtro_eletronicos, transformacao_fn = transformacao_total_vendas)
for item in relatorio_eletronicos:
    print(item)
