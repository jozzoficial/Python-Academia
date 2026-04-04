# Exercício 2.2: Implementação de um retry Decorator

import time
import random


def retry(max_tentativas=3, atraso_segundos=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for tentativa in range(1, max_tentativas + 1):
                try:
                    print(f"Tentativa {tentativa} de {max_tentativas} para {func.__name__}...")
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Falha na tentativa {tentativa}: {e}")
                    if tentativa < max_tentativas: time.sleep(atraso_segundos)
            raise Exception(f"Função {func.__name__} falhou após {max_tentativas} tentativas. ")
        return wrapper
    return decorator


retry(max_tentativas=4, atraso_segundos=0.5)

def operacao_instavel():
    if random.random() < 0.7:  # 70% de chance de falhar
        raise ValueError("Erro simulado na operação!")
    return "Operação bem-sucedida!"


print("\n--- Teste de Operação Instável com Retry ---")
try:
    resultado = operacao_instavel()
    print(f"Resultado final: {resultado}")
except Exception as e: (
    print(f"Erro fatal: {e}"))
