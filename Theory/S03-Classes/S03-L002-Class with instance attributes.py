class Car:
    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK


car_01 = Car('seat', 'ibiza', True, True, True)
car_02 = Car('Opel', 'Corsa', True, True, True)

print(car_01.brand, car_01.model, car_01.isAirBagOK,
      car_01.isPaintingOK, car_01.isMechanicOK)
print(car_02.brand, car_02.model, car_02.isAirBagOK,
      car_02.isPaintingOK, car_02.isMechanicOK)
'''
# def IsCarDamaged (carIsAirBagOK, carIsPaintingOK, carIsMechanicOK):
#     return not (carIsAirBagOK and carIsPaintingOK and carIsMechanicOK)


def IsCarDamaged(aCar):
    return not (aCar['carIsAirBagOK'] and aCar['carIsPaintingOK'] and aCar['carIsMechanicOK'])


# print(IsCarDamaged(car_01['carIsAirBagOK'],car_01['carIsPaintingOK'],car_01['carIsMechanicOK']))
print(IsCarDamaged(car_01))
print(IsCarDamaged(car_02))


cars = [car_01, car_02]

for c in cars:
    print("{} {} damaged = {}".format(c['carBrand'],
        c['carModel'], IsCarDamaged(c)))

'''