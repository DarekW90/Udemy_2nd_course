'''
LAB - Funkcja exec()
Tym razem pracujesz w zwariowanym ośrodku badawczym...

Profesorowie przygotowują swoje skrypty i umieszczają je w określonym katalogu. Twój skrypt ma za zadanie przeczytać te skrypty i je po kolei wykonywać.

Poniżej znajdują się dwa przykładowe skrypty. Każdy z nich skopiuj i zapisz w osobnym pliku (jeżeli wykonanie skryptu miało by być zbyt długie, możesz zmienić ilość iteracji w zmiennej for, ale nie powinno być tak źle):

import math
 
argument_list = []
results_list = []
 
for i in range (1000000):
    argument_list.append(i/10)
    
for x in argument_list:
    results_list.append(abs(math.sin(x) * x**2))
 
print('min = {}  max = {}'.format(min(results_list), max(results_list)))


import math
 
argument_list = []
results_list = []
 
for i in range (1000000):
    argument_list.append(i/10)
    
for x in argument_list:
    results_list.append(abs(x**3 - x**0.5))
 
print('min = {}  max = {}'.format(min(results_list), max(results_list)))
Utwórz listę zawierającą ścieżki dostępu do skryptów:

files_to_process = [
    r"C:\Python\math_sin_square.py",
    r"C:\Python\math_square_root.py"
    ]
Dla każdego pliku:

wyświetl nazwę pliku (skorzystaj z funkcji os.path.basename z modułu os)

otwórz dany plik i wczytaj go do zmiennej source

Wykonaj ten skrypt


'''


import os

files_to_process = [
    r"G:\Cwiczenia\BackEnd\Python\Kurs Udemy\Kurs2\Practice\S01-variables and code\s01-L014_expyr_folder\math_sin_square.py",
    r"G:\Cwiczenia\BackEnd\Python\Kurs Udemy\Kurs2\Practice\S01-variables and code\s01-L014_expyr_folder\math_square_root.py"
    ]

for file_path in files_to_process:

    with open(file_path, 'r') as f:
        print('File {} ...'.format(os.path.basename(file_path)))
        source = f.read()
        exec(source)