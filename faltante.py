

class Conjunto:
    def __init__(self):
          self.conjunto = set(range(1,101))
    def extraer(self, numero):
        if isinstance(numero, int):
            if numero >100:
                raise Exception("El número ingresado es mayor a 100")
            else:
                self.conjunto.remove(numero)
                return self.conjunto
                    
    def calcular_faltante(self):
        if(len(self.conjunto) == 100):
            raise Exception("El conjunto no tiene faltante")
        else:
            #calcula el numero faltante despues de extraer un numero
            for i in range(1,101):
                print(self.conjunto)
                if i not in self.conjunto:
                    return i
                



