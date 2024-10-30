from salondechat import SalonDeChat
from usuario import Usuario

# Ejecución principal
if __name__ == "__main__":
    s = SalonDeChat()

    u = Usuario(s)
    u.set_nombre("Juan")
    s.registra(u)

    u1 = Usuario(s)
    u1.set_nombre("Pepe")
    s.registra(u1)

    u2 = Usuario(s)
    u2.set_nombre("Pedro")
    s.registra(u2)

    u.envia("Pepe", "Hola como andas?")
    u1.envia("Juan", "Todo ok, vos?")
    u2.envia("Martin", "Martin estas?")
