class Car:

    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        Car.numberOfCars += 1
        Car.listOfCars.append(self)

    def IsDamaged(self):
        return not (self.isAirBagOK and self.isPaintingOK and self.isMechanicOK)

    def GetInfo(self):
        print('{} {}'.format(self.brand, self.model).upper())
        print('Air Bag  - ok -  {}'.format(self.isAirBagOK))
        print('Painting - ok -  {}'.format(self.isPaintingOK))
        print('Mechanic - ok -  {}'.format(self.isMechanicOK))
        print('-'*30)


print('Class level variables BEFORE creating instances:',
      Car.numberOfCars, Car.listOfCars)


car_01 = Car('seat', 'ibiza', True, True, True)
car_02 = Car('Opel', 'Corsa', True, False, True)

print('Class level variables AFTER creating instances:',
      Car.numberOfCars, Car.listOfCars)

print('Id of class is:', id(Car))
print('Id of instance are:', id(car_01), id(car_02))

print('Check if object belongs to class:', isinstance(car_01, Car))
print('Check if object belongs to class using type:', type(car_01) is Car)
print('Check class of and object using __class__:', car_01.__class__)

print('List of instance attributes with values', vars(car_01))
print('List of class attributes with values:      ', vars(Car))

print('List of instance attributes with values', dir(car_01))
print('List of class attributes with values:      ', dir(Car))

#Car.numberOfCars = 123

print('Value taken from instance:', car_01.numberOfCars, 'Value taken from class', Car.numberOfCars)

