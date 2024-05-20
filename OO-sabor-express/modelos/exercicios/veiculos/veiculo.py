from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self,  marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f"{self.marca} {self.modelo} - Status: {status}"
    
    @abstractmethod
    def ligar(self):
        pass

       # if not self._ligado: 
       #     modo = 'Ligado'
       # else:
       #     modo = 'desligado'    
       # return f'marca: {self.marca} | modelo: {self.modelo} | estado: {modo}'