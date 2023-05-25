# carBrand = 'Seat'
# carModel = 'Ibiza'
# carIsAirBagOK = True
# carIsPaintingOK = True
# carIsMechanicOK = True

car_01 = {
    'carBrand': 'Seat',
    'carModel': 'Ibiza',
    'carIsAirBagOK': True,
    'carIsPaintingOK': True,
    'carIsMechanicOK': True
}
car_02 = {
    'carBrand': 'Opel',
    'carModel': 'Corsa',
    'carIsAirBagOK': True,
    'carIsPaintingOK': False,
    'carIsMechanicOK': True
}

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
