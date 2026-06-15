#Problema: Padronizar datas em um texto de DD/MM/AAAA para AAAA-MM-DD e
#capitalizar a primeira letra de cada frase.

import re


def formatar_data(match):
    dia = match.group(1)
    mes = match.group(2)
    ano = match.group(3)

    return f"{ano}-{mes}-{dia}"


def capitalizar_frase(match):
    # match.group(0) é a frase inteira, incluindo o ponto final
    return match.group(0).capitalize()


texto_original = (
    "Hoje é 26/10/2023. amanhã será 27/10/2023. "
    "o prazo final é 31/12/2023."
)

print("\n--- Refatoração de Texto com Regex ---")

# 1. Padronizar datas
texto_datas_formatadas = re.sub(
    r"(\d{2})/(\d{2})/(\d{4})",
    formatar_data,
    texto_original
)

print(f"Texto com datas formatadas: {texto_datas_formatadas}")

# Saída:
# Hoje é 2023-10-26. amanhã será 2023-10-27.
# o prazo final é 2023-12-31.

# 2. Capitalizar a primeira letra de cada frase
# Procura por um ponto final seguido de espaço e uma letra minúscula
# Usa lookbehind (?<=[.?!]\s) para garantir que o ponto e espaço
# estão lá, mas não os inclui na substituição
# Usa \b para limite de palavra para garantir que não capitaliza
# no meio de uma palavra

texto_final = re.sub(
    r"(?<=[.?!]\s)([a-z])",
    lambda m: m.group(1).upper(),
    texto_datas_formatadas
)

# Capitalizar a primeira letra da primeira frase (se necessário)
if texto_final and texto_final[0].islower():
    texto_final = texto_final[0].upper() + texto_final[1:]

print(f"Texto final formatado: {texto_final}")

# Saída:
# Hoje é 2023-10-26. Amanhã será 2023-10-27.
# O prazo final é 2023-12-31.