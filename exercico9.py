#Problema: Desenvolver um sistema para gerenciar diferentes tipos de itens numa biblioteca
#(livros, revistas), aplicando herança e polimorfismo para lidar com as particularidades de cada tipo



class ItemBiblioteca:
    def __init__(self, titulo, autor_ou_editora, ano_publicacao):
        self.titulo = titulo
        self.autor_ou_editora = autor_ou_editora
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"'{self.titulo}' emprestado com sucesso.")
        else:
            print(f"'{self.titulo}' não está disponível para empréstimo.")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"'{self.titulo}' devolvido com sucesso.")
        else:
            print(f"'{self.titulo}' já está disponível.")

    def exibir_detalhes(self):
        status = "Disponível" if self.disponivel else "Emprestado"

        print(f"Título: {self.titulo}")
        print(f"Autor/Editora: {self.autor_ou_editora}")
        print(f"Ano: {self.ano_publicacao}")
        print(f"Status: {status}")


class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor, ano_publicacao, isbn):
        super().__init__(titulo, autor, ano_publicacao)
        self.isbn = isbn

    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f"ISBN: {self.isbn}")


class Revista(ItemBiblioteca):
    def __init__(self, titulo, editora, ano_publicacao, numero_edicao):
        super().__init__(titulo, editora, ano_publicacao)
        self.numero_edicao = numero_edicao

    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f"Edição: {self.numero_edicao}")


class Biblioteca:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)
        print(f"Item '{item.titulo}' adicionado à biblioteca.")

    def listar_itens(self):
        print("\n--- Itens na Biblioteca ---")

        for item in self.itens:
            item.exibir_detalhes()  # Polimorfismo em ação
            print("-" * 20)
            biblioteca = Biblioteca()

            livro1 = Livro(
                "Python para Iniciantes",
                "João Silva",
                2024,
                "978-1234567890"
            )

            revista1 = Revista(
                "Tecnologia Hoje",
                "Editora Tech",
                2025,
                15
            )

            biblioteca.adicionar_item(livro1)
            biblioteca.adicionar_item(revista1)

            biblioteca.listar_itens()

            livro1.emprestar()
            livro1.devolver()