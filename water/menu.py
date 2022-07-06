from service.water_billing_service import  WaterBillingService
from console.UI_water_consumption import UIWaterConsumption
from console.UI_debt_check import WaterUIDebtCheck
from console.UI_member_register import UIMemberRegister
class Menu:

    def __init__(self):
        self.billing_service =  WaterBillingService("Coperativa local de AGUA")

    def process_run(self):
        self.show_main_menu()
        option = int(input('Ingrese una opcion: '))
        should_exit = False

        if option == 1:
            self.register_consumption()
        elif option == 2:
            self.show_debt_amout()
        elif option == 3:
            pass
        elif option == 4:
            pass
        elif option == 5:
            self.register_member()

        elif option == 6:
            should_exit = True

        else:
            print('Invalid Option')

        return should_exit

    def register_consumption(self):
        UI = UIWaterConsumption(self.billing_service)
        UI.register_consumption()

    def show_debt_amout(self):
        UI = WaterUIDebtCheck(self.billing_service)
        UI.processs()

    def register_member(self):
        UI = UIMemberRegister(self.billing_service)
        UI.processs()

    def show_main_menu(self):
        print('''
        COPERATIVA LOCAL DE AGUA
        
        -----------------------------------------
        1. Registrar consumo de agua
        2. Consultar deuda de socio
        3. Consultar detalles de Socio
        4. Realizar Cobro
        5. Registrar miembro
        6. Exit
        -----------------------------------------
        ''')