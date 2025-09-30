class Produto: 
   contador_id = 1 #variável dentro da classe

   def __init__(self, nome, marca, quantidade, preco_unitario): #Isso é o construtor da classe __init__
        self.id = Produto.contador_id
        Produto.contador_id += 1

        self.nome = nome
        self.marca = marca
        self.quantidade = quantidade
        self.valor = preco_unitario 
   
   def __str__(self):
       return f"[{self.id}] {self.nome} | {self.marca} | {self.quantidade} | R${self.valor:.2f}"

   def total(self):
       return self.quantidade * self.valor