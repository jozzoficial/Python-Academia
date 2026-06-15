#Problema: Construir uma árvore de expressão a partir de uma expressão aritmética simples
#(apenas adição e multiplicação) e avaliá-la.
class NoExpressao:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


def construir_arvore_expressao(expressao_tokens):
    # Simplificação: assume que a expressão já está em notação pós-fixa (RPN)
    # Para uma solução completa, seria necessário um parser para converter infix para postfix

    pilha = []
    operadores = {"+", "*"}

    for token in expressao_tokens:
        if token not in operadores:
            # Operando
            pilha.append(NoExpressao(int(token)))
        else:
            # Operador: requer dois operandos da pilha
            direita = pilha.pop()
            esquerda = pilha.pop()

            no_operador = NoExpressao(token)
            no_operador.esquerda = esquerda
            no_operador.direita = direita

            pilha.append(no_operador)

    # A raiz da árvore é o último elemento na pilha
    return pilha.pop()


def avaliar_arvore_expressao(no):
    if no.valor not in {"+", "*"}:
        # É um operando (número)
        return no.valor
    else:
        val_esquerda = avaliar_arvore_expressao(no.esquerda)
        val_direita = avaliar_arvore_expressao(no.direita)

        if no.valor == "+":
            return val_esquerda + val_direita
        elif no.valor == "*":
            return val_esquerda * val_direita


# Exemplo de uso: Expressão (3 + 4) * 5 em notação pós-fixa
expressao_rpn = ["3", "4", "+", "5", "*"]  # Equivalente a (3 + 4) * 5

print("\n--- Árvore de Expressão Aritmética ---")

arvore = construir_arvore_expressao(expressao_rpn)
resultado = avaliar_arvore_expressao(arvore)

print(f"Expressão RPN: {expressao_rpn}")
print(f"Resultado da avaliação: {resultado}")  # Saída: 35


# Outro exemplo: (10 * 2) + (5 * 3)
expressao_rpn2 = ["10", "2", "*", "5", "3", "*", "+"]

arvore2 = construir_arvore_expressao(expressao_rpn2)
resultado2 = avaliar_arvore_expressao(arvore2)

print(f"Expressão RPN: {expressao_rpn2}")
print(f"Resultado da avaliação: {resultado2}")  # Saída: 35