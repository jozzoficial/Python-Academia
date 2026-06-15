#Problema: Criar uma classe que represente uma sequência numérica personalizada e que possa
#ser iterada diretamente com um loop for

class SequenciaNumerica:
    def __init__(self, inicio, fim, passo=1):
        self.inicio = inicio
        self.fim = fim
        self.passo = passo
        self._current = inicio  # Estado interno para a iteração

    def __iter__(self):
        # Torna o objeto iterável
        self._current = self.inicio  # Reinicia o iterador
        return self

    def __next__(self):
        # Define como o próximo item é obtido
        if self._current < self.fim:
            valor = self._current
            self._current += self.passo
            return valor
        else:
            raise StopIteration  # Sinaliza o fim da iteração

    def __len__(self):
        if self.passo == 0:
            return 0

        return max(
            0,
            (self.fim - self.inicio + self.passo - 1) // self.passo
        )

    def __getitem__(self, index):
        if isinstance(index, slice):
            # Lidar com fatiamento (slice)
            start = index.start if index.start is not None else 0
            stop = index.stop if index.stop is not None else self.__len__()
            step = index.step if index.step is not None else 1

            # Calcular os valores do slice
            valores = []

            for i in range(start, stop, step):
                if i < 0 or i >= self.__len__():
                    raise IndexError("Índice fora do limite")

                valores.append(self.inicio + i * self.passo)

            if valores:
                return SequenciaNumerica(
                    valores[0],
                    valores[-1] + self.passo,
                    self.passo
                )
            else:
                return SequenciaNumerica(0, 0)

        else:
            # Lidar com acesso por índice único
            if index < 0 or index >= self.__len__():
                raise IndexError("Índice fora do limite")

            return self.inicio + index * self.passo


# Exemplo de uso
seq = SequenciaNumerica(1, 10, 2)

print("\n--- Iterador Personalizado ---")
print("Iterando com for:")

for num in seq:
    print(num, end=" ")  # Saída: 1 3 5 7 9

print()

print(f"Comprimento da sequência: {len(seq)}")

# Acesso por índice
print(f"Elemento no índice 2: {seq[2]}")

# Fatiamento
subseq = seq[1:4]

print("Subsequência:")
for num in subseq:
    print(num, end=" ")