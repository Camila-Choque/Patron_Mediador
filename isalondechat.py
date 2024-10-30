#Mediador: : define una interface para comunicarse con los objetos colegas.
from usuario import Usuario

# Interfaz de salón de chat
class ISalonDeChat:
    def registra(self, participante: Usuario):
        pass

    def envia(self, de: str, a: str, msg: str):
        pass
