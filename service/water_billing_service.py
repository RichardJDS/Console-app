from model.member_list import MemberList
from model.member import Member
from model.water_consumption import WaterConsumption
from datetime import datetime
class WaterBillingService:
    price = 3
    def __init__(self, title):
        self._title = title
        self.members = MemberList()
        self.consumptionDB = []

    @property
    def title(self):
        return self._title

    def register_member(self, nombre):
        new_member = Member(nombre)
        self.members.add_member(new_member)

    def find_member_id(self, nombre):
        return self.members.get_member_id(nombre)

    def register_consumption(self, member_id, consumption):
        self.consumptionDB.append(WaterConsumption(member_id, consumption,datetime.today()))

    def calculate_debt(self, member_id):
        total_debt = 0
        for consumo_member in self.consumptionDB:
            if consumo_member.id == member_id:
                total_debt +=  consumo_member.mes_consumption
        return total_debt

if __name__ == '__main__':
    waterBill1 = WaterBillingService('Facturacion de agua')
    waterBill1.register_member('Richard')
    waterBill1.register_member('Jhony')
    waterBill1.register_member('oso')
    print(waterBill1.find_member_id('oso'))
    for member in waterBill1.members.members:
        print(member)
    waterBill1.register_consumption(1001, 50)
    waterBill1.register_consumption(1002, 100)
    waterBill1.register_consumption(1001, 50)
    waterBill1.register_consumption(1001, 50)
    for consumo in waterBill1.consumptionDB:
        print(consumo)

    print(f'Deuda total: {waterBill1.calculate_debt(1001)}')