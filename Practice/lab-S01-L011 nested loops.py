'''
Postanawiasz otworzyć linie lotnicze "Flying Python". Linie będą krajowe. Oto wykaz portów lotniczych:

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
1. Zbuduj listę tupletów symbolizujących port początkowy i końcowy. Wykonaj połączenie każdy-z-każdym

2. Wyeliminuj z powyższej listy połączenie z portu do tego samego portu

3. Ponieważ połączenie z A do B dubluje się z połączeniem z B do A - wygeneruj możliwe połączenia krajowe pomijając takie zdublowane trasy.

4. Policz ilość generowanych połączeń w krokach 1,2,3

'''

# wykonanie moje #

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

print("Odpowiedz 1")
conections1 = [(a, b)for a in ports for b in ports]
print(conections1)
print()
print("Odpowiedz 2")
conections2 = [(a, b)for a in ports for b in ports if a != b]
print(conections2)
print()
print("Odpowiedz 3")
conections3 = [(a, b)for a in ports for b in ports if b != a]
print(conections3)
print()
print("Odpowiedz 4")
conections4 = conections1 + conections2 + conections3
print("Ilość generowanych połączeń w krokach 1,2,3:", len(conections4))


# wykonanie instruktora
print('*'*50)
ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
 
routes = [ (start, stop) for start in ports for stop in ports]
print(routes)
print(len(routes))
 
routes = [ (start, stop) for start in ports for stop in ports if start != stop]
print(routes)
print(len(routes))
 
 
routes = [ (start, stop) for start in ports for stop in ports if start < stop]
print(routes)
print(len(routes))