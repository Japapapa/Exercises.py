# 1: Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.

# 1-)

# class Restaurante:
#     nome = ''
#     categoria = ''
#     ativo = False

# restaurante_praca = Restaurante()
# restaurante_praca.categoria = 'Italiano'

# print(restaurante_praca.categoria)

# ====================================

# 2: Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.

# 2-)

# class Restaurante:
#     nome = ''
#     categoria = ''
#     ativo = False

# restaurante_praca = Restaurante()
# restaurante_praca.nome = "Restaurante da Praça"

# nome_restaurante = restaurante_praca.nome

# print(nome_restaurante)

# ====================================

# 3: Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.

# 3-)

# class Restaurante:
#     nome = ''
#     categoria = ''
#     ativo = True


# restaurante_praca = Restaurante()
# status = restaurante_praca.ativo

# nome_restaurante1 = restaurante_praca.nome

# restaurante_praca.nome = "Restaurante da Praça"

# if status == False:
#     print(f"O restaurante {nome_restaurante1}está fechado!")
# else:
#     print(f"O restaurante {nome_restaurante1}está aberto!")
#

# ================================

# 4: Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria. 


# class Restaurante:
#     nome = ''
#     categoria = ''
#     ativo = False

# Restaurante.categoria = 'Italiano'
# categoria = Restaurante.categoria

# print(categoria)

# =================================

# 5: Altere o valor do atributo nome para 'Bistrô'.

# 5-)

# class Restaurante:
#     nome = ''
#     categoria = ''
#     ativo = False

# restaurante_praca = Restaurante()
# restaurante_praca.nome = "Restaurante da Praça"

# nome_restaurante = restaurante_praca.nome
# restaurante_praca.nome = 'Bistrô'
# novo_nome = restaurante_praca.nome
# print(novo_nome)

# ===================================

# 6: Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.

# 6-)

# class Restaurante:
#     nome = ''
#     categoria = ''
#     ativo = False

# restaurante_pizza = Restaurante()
# restaurante_pizza.nome = "Pizza Place"
# restaurante_pizza.categoria = 'Fast Food'

# ----------------
# obs: criar um banco de dados que registra a categoria para futuros restaurantes
# ----------------

# =====================================

# 7: Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.

# 7-)
# class Restaurante:
#     nome = ''
#     categoria = ''
#     ativo = False

# restaurante_pizza = Restaurante()
# restaurante_pizza.nome = "Pizza Place"
# nome = restaurante_pizza.nome
# restaurante_pizza.categoria = 'Fast Food'

# categoria = restaurante_pizza.categoria

# print(f"A categoria de {nome} é {categoria}")

# =======================================

# 8: Mude o estado da instância restaurante_pizza para ativo.

# 8-)

# class Restaurante:
#     nome = ''
#     categoria = ''
#     ativo = False

# restaurante_pizza = Restaurante()
# restaurante_pizza.ativo = True
# restaurante_pizza.nome = "Pizza Place"
# nome = restaurante_pizza.nome
# restaurante_pizza.categoria = 'Fast Food'

# categoria = restaurante_pizza.categoria

# status = restaurante_pizza.ativo

# if status != False:
#     print(f"A categoria de {nome} é {categoria} e está ativo!")

# ===============================

# 9:Imprima no console o nome e a categoria da instância restaurante_praca.

# 9-)
# class Restaurante:
#     nome = ''
#     categoria = ''
#     ativo = False

# restaurante_praca = Restaurante()
# restaurante_praca.nome = "Restaurante da Praça"
# restaurante_praca.categoria = "Italiana"
# categoria = restaurante_praca.categoria

# nome_restaurante = restaurante_praca.nome
# restaurante_praca.nome = 'Bistrô'
# novo_nome = restaurante_praca.nome


# print(f"Restaurante: {novo_nome}, Categoria: {categoria}")
