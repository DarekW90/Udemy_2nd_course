'''
W tym zadaniu będziesz pracować z następującą  listą:

    text_list = ['x','xxx','xxxxx','xxxxxxx','']

1. Przygotuj i zapisz w zmiennej f  funkcję lambda, która dla argumentu będącego napisem zwróci jego długość
2. Przetestuj działanie funkcji na dowolnym napisie
3. Uruchom funkcję f na każdym elemencie listy text_list. Wykorzystasz przy tym funkcję map, która pozwala uruchomić wskazywaną przez pierwszy argument funkcję dla listy przekazanej jako drugi argument.
Uwaga: funkcja map nie zwraca listy, ale zwracany obiekt można łatwo skonwertować do listy.
4. Zmień wywołanie  funkcji map tak, żeby funkcja nie była zapisywana w zmiennej f, ale zamiast tego definiowana dynamicznie w wywołaniu funkcji map
'''


f = lambda x:len(x)
print(f('a 19-letters string'))

text_list = ['x','xxx','xxxxx','xxxxxxx','']

print(list(map(f,text_list)))

print(list(map(lambda s:len(s),text_list)))