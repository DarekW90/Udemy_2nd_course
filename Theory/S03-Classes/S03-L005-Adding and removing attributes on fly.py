class Car:

    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        self.__isOnSale = isOnSale
        Car.numberOfCars += 1
        Car.listOfCars.append(self)

    def IsDamaged(self):
        return not (self.isAirBagOK and self.isPaintingOK and self.isMechanicOK)

    def GetInfo(self):
        print('{} {}'.format(self.brand, self.model).upper())
        print('Air Bag  - ok -  {}'.format(self.isAirBagOK))
        print('Painting - ok -  {}'.format(self.isPaintingOK))
        print('Mechanic - ok -  {}'.format(self.isMechanicOK))
        print('IS ON SALE       {}'.format(self.__isOnSale))
        print('-'*30)


car_01 = Car('seat', 'ibiza', True, True, True, False)
car_02 = Car('Opel', 'Corsa', True, False, True, True)

# car_02.__isOnSale = False
car_02._Car__isOnSale = False
car_02.YearOfProduction = 2005
del car_02.YearOfProduction

print('-'*20)
setattr(car_02, 'TAXI', False)
print(hasattr(car_02, 'TAXI'))
print('-'*20)
delattr(car_02, 'TAXI')
print(hasattr(car_02, 'TAXI'))
print('-'*20)

car_02.GetInfo()
print(vars(car_02))
