#Exercício 2.1: Ordenação Personalizada com lambda e sorted

pessoas = [
    {"nome": "Ana", "idade": 30},
    {"nome": "Bruno", "idade": 25},
    {"nome": "Carla", "idade": 30},
    {"nome": "Daniel", "idade": 25},
    {"nome": "Eduardo", "idade": 35}
]

# Ordenar usando uma função lambda com múltiplos critérios
pessoas_ordenadas = sorted(pessoas, key=lambda p: (p["idade"], p["nome"]))
print("\n--- Pessoas Ordenadas ---")
for pessoa in pessoas_ordenadas:
    print(pessoa)  # Saída esperada:
# {"nome": "Bruno", "idade": 25}
# {"nome": "Daniel", "idade": 25}
# {"nome": "Ana", "idade": 30}
# {"nome": "Carla", "idade": 30} 
# {"nome": "Eduardo", "idade": 35}
