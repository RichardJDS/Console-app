class Member:
    contador_member = 1000
    def __init__(self, nombre):
        Member.contador_member += 1
        self.id = Member.contador_member
        self.nombre = nombre
    def __str__(self):
        return f'ID: {self.id} Nombre: {self.nombre}'