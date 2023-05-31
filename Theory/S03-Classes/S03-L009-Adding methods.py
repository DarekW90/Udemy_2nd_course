import csv
import types


def exportToFile_Static(path, header, data):
    with open(path, mode='w') as file:
        writer = csv.writer(file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerow(data)
    # just to see that the function was indeed called:
    print('>>>> This is function exportToFile - static method')


def exportToFile_Class(cls, path):
    with open(path, mode='w') as file:
        writer = csv.writer(file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['brand', 'model', 'IsOnSale'])
        for c in cls.listOfCars:
            writer.writerow([c.brand, c.model, c.IsOnSale])
    # just to see that the function was indeed called:
    print('>>>> This is function exportToFile - class method')


def exportToFile_Instance(self, path):
    with open(path, mode='w') as file:
        writer = csv.writer(file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['brand', 'model', 'IsOnSale'])
        writer.writerow([self.brand, self.model, self.IsOnSale])
    # just to see that the function was indeed called:
    print('>>>> This is function exportToFile - instance method')


brandOnSale = 'Opel'


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

    def __GetIsOnSale(self):
        return self.__isOnSale

    def __SetIsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print('Changing status IsOnSale to {} for {}'.format(
                newIsOnSaleStatus, self.brand))
        else:
            print('Cannot change status IsOnSale. Sale valid only for {}'.format(
                brandOnSale))

    IsOnSale = property(__GetIsOnSale, __SetIsOnSale, None,
                        'if set to true, the car is available in sale/promo')


car_01 = Car('Seat', 'Ibiza', True, True, True, False)
car_02 = Car('Opel', 'Astra', True, True, True, False)

print('Static------------'*10)
Car.ExportToFile_Static = exportToFile_Static
# exportToFile_Static(f'G:\.Cwiczenia\BackEnd\Python\Kurs Udemy\Kurs2\Theory\S03-Classes\Data\S03-L009\export_static.csv',['Brand','Model','IsOnsale'], [car_01.brand,car_01.model,car_01.IsOnSale])
Car.ExportToFile_Static(f'G:\.Cwiczenia\BackEnd\Python\Kurs Udemy\Kurs2\Theory\S03-Classes\Data\S03-L009\export_static.csv',
                        ['Brand', 'Model', 'IsOnsale'], [car_01.brand, car_01.model, car_01.IsOnSale])
print(dir(Car))


print('Class-------------'*10)
# Car.ExportToFile_Class = exportToFile_Class
Car.ExportToFile_Class = types.MethodType(exportToFile_Class, Car)
Car.ExportToFile_Class(
    path=f'G:\.Cwiczenia\BackEnd\Python\Kurs Udemy\Kurs2\Theory\S03-Classes\Data\S03-L009\export_Class.csv')
print(dir(Car))

print('Instance----------'*10)
# car_01.ExportToFile_Instance = exportToFile_Instance
car_01.ExportToFile_Instance = types.MethodType(exportToFile_Instance, car_01)
car_01.ExportToFile_Instance(
    path=f'G:\.Cwiczenia\BackEnd\Python\Kurs Udemy\Kurs2\Theory\S03-Classes\Data\S03-L009\export_instance.csv')
print(dir(car_01))

print('-'*50)
if hasattr(car_01, 'ExportToFile_Static') and callable(car_01.ExportToFile_Static):
    print("The object has method ExportToFile_Static")
if hasattr(car_01, 'ExportToFile_Class') and callable(car_01.ExportToFile_Class):
    print("The object has method ExportToFile_Class")
if hasattr(car_01, 'ExportToFile_Instance') and callable(car_01.ExportToFile_Instance):
    print("The object has method ExportToFile_Instance")
else:
    print('no such method!')
