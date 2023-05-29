'''
Pracujemy z wynikiem LAB z poprzedniej lekcji.

Dodaj do klasy Cake atrybut na poziomie klasy. Nazwij go known_types. Będą w nim przechowywane produkowane w naszej cukierni słodkości. Przypisz do zmiennej listę np. w następującej postaci:

    ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']

Zmień __init__ tak, że jeżeli jako parametr kind zostanie przekazana wartość znajdująca się na liście known_kinds, to zostanie zaakceptowana, ale jeśli ktoś przekaże wartość spoza tej listy, to do nowo tworzonego obiektu do atrybutu kind zostanie wpisany napis other.

Przetestuj działanie nowej funkcji __init__ tworząc obiekt "wafel kakaowy":

    cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa')


Dodaj do klasy Cake nowy atrybut bakery_offer, który na początku będzie pustą listą.
Zmień __init__ tak, aby po utworzeniu nowego obiektu typu Cake, został on automatycznie dodany do listy bakery_offer
Usuń ze skryptu niepotrzebne już instrukcje tworzące listę bakery_offer i dodające obiekty tej klasy do tej listy.
Zmień pętlę wyświetlającą informację o ofercie cukierni tak, aby korzystała z atrybutu klasy

Sprawdź czy obiekty cake01 i inne są instancjami klasy Cake korzystając z funkcji isinstance i type

Wyświetl informacje o instancji cake01 i o klasie Cake korzystając z funkcji vars i dir

'''

know_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
bakery_offer = []

class Cake:
    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling

    def show_info(self):
        print('{}'.format(self.name).upper())
        print('Kind: {}'.format(self.kind))
        print('Taste: {}'.format(self.taste))
        if len(self.additives) > 0:
            print('Additives:')
            for a in self.additives:
                print('\t{}'.format(a))
        if len(self.filling) > 0:
            print('Filling: {}'.format(self.filling))
        print('-'*30)

    def set_filling (self, filling):
        self.filling = filling
    
    def add_additives(self, additives):
        self.additives.extend(additives)

cake_01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream')
cake_02 = Cake('Chocolate Muffin', 'muffin', 'chocolate', ['chocolate'], '')
cake_03 = Cake('Super Sweet Maringue', 'maringue', 'very sweet', [], '')

bakery_offer = []
bakery_offer.append(cake_01)
bakery_offer.append(cake_02)
bakery_offer.append(cake_03)

cake_02.set_filling('vanilla cream')
cake_03.add_additives(['coca powder', 'coconuts'])

print('='*30)
print('Today in our offer:')
for c in bakery_offer:
    c.show_info()

print('Is cake_01 of type Cake (isinstance)', isinstance(cake_01, Cake))
print('Is cake_01 type of Cake? (type)', type(cake_01) is Cake)
print('Vars cake_01', vars(cake_01))
print('vars Cake?', vars(Cake))
print('dir cake_01', dir(cake_01))
print('dir Cake?', dir(Cake))
