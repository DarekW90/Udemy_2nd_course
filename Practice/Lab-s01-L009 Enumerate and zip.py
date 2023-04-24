"""
LAB - enumerate & zip
Utwórz następujące listy:

projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

Korzystając ze "sprytnej" metody pracy z for wyświetl komunikaty w postaci:

The leader of "...nazwa projektu..." is ...imię i nazwisko lidera...

============================================================================

Utwórz kolejną listę z datami rozpoczęcia projektów:

dates = ['2016-06-23', '2016-08-29', '1994-01-01']

The leader of "...nazwa projektu..."  started ...data rozpoczęcia projektu... is ...imię i nazwisko lidera...

Korzystając ze "sprytnego" złożenia enumerate i zip - dodaj do komunikatu dodatkowo numer kolejny projektu rozpoczynając od 1:
...numer kolejny... - The leader of "...nazwa projektu..."  started ...data rozpoczęcia projektu... is ...imię i nazwisko lidera...
"""

projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
dates = ['2016-06-23', '2016-08-29', '1994-01-01']

data = list(zip(projects, leaders))

for p, l in data:
    print('The leader of',p, 'is', l )

print('*'*30)

for pos, (p,d,l) in enumerate(zip(leaders,dates, leaders)):
    print(pos +1,':','The leader of',p, 'started',d,'is', l )


print('*'*10, 'Wykonanie instruktora','*'*10 )

projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
 
for p, l in zip(projects, leaders):
    print('The leader of "{}" is {}'.format(p,l))
 
print('*'*30)
dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for p, l,d in zip(projects, leaders, dates):
    print('The leader of "{}" started {} is {}'.format(p,d,l))
print('*'*30)
 
for i, (p,l,d) in enumerate(zip(projects, leaders, dates)):
    print('{} - The leader of "{}" started {} is {}'.format(i+1,p,d,l))