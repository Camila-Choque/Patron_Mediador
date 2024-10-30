#Mediador Concreto: : implementa la interface y define como los colegas se comunican entre ellos
from isalondechat import ISalonDeChat
from usuario import Usuario
from typing import Dict

# Clase Salón de Chat
class SalonDeChat(ISalonDeChat):
    def __init__(self):
        self.participantes: Dict[str, Usuario] = {}

    def registra(self, user: Usuario):
        self.participantes[user.get_nombre()] = user

    def envia(self, de: str, a: str, msg: str):
        if de in self.participantes and a in self.participantes:
            u = self.participantes[a]
            u.recibe(de, msg)
        else:
            print("Usuario inexistente")

