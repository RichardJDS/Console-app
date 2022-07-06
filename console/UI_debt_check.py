class WaterUIDebtCheck:
    def __init__(self, system):
        self.system = system

    def processs(self):
        print(' '.center(50, '-'))
        id = int(input('Ingrese el codigo de usuario: '))
        try:
            debt = self.system.calculate_debt(id)
            print(f'La deuda del socio {id} es de {debt} Bs')
        except Exception as ex:
            print('Ocurrio un error', ex)
