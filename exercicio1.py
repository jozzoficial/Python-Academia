#Problema: Dada uma string contendo parênteses, chavetas e colchetes, determine se os
#símbolos estão balanceados (ou seja, cada abertura tem um fechamento correspondente na
#ordem correta)
def verificar_parenteses_balanceados(expressao):
    pilha = []

    # Mapeia fechamento para abertura
    mapeamento = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in expressao:
        # É um parêntese de abertura
        if char in mapeamento.values():
            pilha.append(char)

        # É um parêntese de fechamento
        elif char in mapeamento.keys():
            if not pilha or mapeamento[char] != pilha.pop():
                return False  # Pilha vazia ou não corresponde ao topo

    # Retorna True se a pilha estiver vazia no final
    return not pilha


# Exemplos de uso
print("\n--- Verificação de Parênteses Balanceados ---")

print(f"{{[()]}}: {verificar_parenteses_balanceados('{[()]}')}")
# Saída: True

print(f"{{[(])}}: {verificar_parenteses_balanceados('{[(])}')}")
# Saída: False

print(f"((())) : {verificar_parenteses_balanceados('((()))')}")
# Saída: True

print(f"(() : {verificar_parenteses_balanceados('(()')}")
# Saída: False

print(f"}} : {verificar_parenteses_balanceados('}')}")
# Saída: False