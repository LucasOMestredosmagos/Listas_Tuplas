class Numero:
    def __init__(self):
        self.valores = []
        self.pares = []
        self.impares = []
    
    def solicitar_valores(self):
        for i in range(10):
            valor = int(input(f"Digite o valor {i+1}: "))
            self.valores.append(valor) 
    
    def separar_pares_impares(self):
        for valor in self.valores:
            if valor % 2 == 0:
                self.pares.append(valor)
            else:
                self.impares.append(valor)
    
    def exibir_resultados(self):
        print('Números pares:', self.pares) 
        print('Números ímpares:', tuple(self.impares))   
        print('Quantidade de números pares:', len(self.pares))   
        print('Quantidade de números ímpares', len(self.impares))   
        print('Soma dos números pares:', sum(self.pares))
        print('Soma dos números ímpares:', sum(self.impares))
        
numero = Numero()

numero.solicitar_valores()
numero.separar_pares_impares()
numero.exibir_resultados()        