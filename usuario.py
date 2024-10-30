# Colleague Concreto: cada colega conoce su mediador, y lo usa para comunicarse con otros colegas.
from iusuariochat import IUsuarioChat

# Clase Usuario
class Usuario(IUsuarioChat):
    def __init__(self, salon_de_chat: "ISalonDeChat"): #forward references
        self.nombre = ""
        self.salon = salon_de_chat

    def recibe(self, de: str, msg: str):
        s = f"el usuario {de} te dice: {msg}"
        print(f"{self.nombre}: {s}")

    def envia(self, a: str, msg: str):
        self.salon.envia(self.nombre, a, msg)

    def get_nombre(self) -> str:
        return self.nombre

    def set_nombre(self, nombre: str):
        self.nombre = nombre
