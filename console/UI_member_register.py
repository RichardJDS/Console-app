from service.water_billing_service import WaterBillingService
class UIMemberRegister:
    def __init__(self, billing_service):
        self.billing_service = billing_service

    def processs(self):
        print(' '.center(50, '-'))
        print(' '.center(50, '-'))
        nombre = input('Ingrese el nombre del socio: ')
        try:
            self.billing_service.register_member(nombre)
            print(f'El Nuevo socio {nombre} ha sido registrado exitosamente')
        except Exception as ex:
            print('Ocurrio un error del tipo', ex)

