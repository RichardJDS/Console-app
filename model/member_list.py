from model.member import Member
class MemberList:
    def __init__(self):
        self.members = []

    def add_member(self, newMember):
        self.members.append(newMember)
    def get_member_id(self, nombre):
        id = 0
        for member in self.members:
            if member.nombre == nombre:
                id = member.id
        if id != 0 :
            return id
        else:

            return 'Cliente no registrado'


