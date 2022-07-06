from service.water_billing_service import WaterBillingService
class UIWaterConsumption:
    def __init__(self, service):
        self.service = service

    def register_consumption(self):
        print(' '.center(50, '-'))
        id = int(input('Ingrese el codigo de usuario: ' ))
        water_consumption = int(input('Ingrese el valor de consumo: '))
        self.service.register_consumption(id, water_consumption)