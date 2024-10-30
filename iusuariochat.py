# Colleague: define el comportamiento que debe implementar cada colega para poder comunicarse el mediador
class IUsuarioChat:
    def recibe(self, de: str, msg: str):
        pass

    def envia(self, a: str, msg: str):
        pass
