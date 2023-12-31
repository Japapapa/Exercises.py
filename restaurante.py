# nome = str("")
# categoria = ("")
# disponivel ou não = bool(True or False)

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self.nome} | {self.categoria}"
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}")

restaurante_praca = Restaurante("Praça", "gourmet")
restaurante_pizza = Restaurante("Pizza express", "italiana")

Restaurante.listar_restaurantes()