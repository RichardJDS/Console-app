class WaterConsumption:
    def __init__(self, id, consumption, fecha):
        self._id = id
        self._mes_consumption = consumption
        self.fecha = fecha

    @property
    def id(self):
        return self._id
    @property
    def mes_consumption(self):
        return self._mes_consumption

    def __str__(self):
        return f'ID : {self._id} costo de consumo: {self._mes_consumption} Fecha: {self.fecha}'

if __name__ == '__main__':
    prueba = WaterConsumption(100, 500, 56)
    print(prueba.id)
