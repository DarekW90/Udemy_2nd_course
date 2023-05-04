"""
Zapisz poniższe polecenie if w postaci uproszczonej:
"""

import datetime
import datetime as dt


price = 123
bonus = 23
bonus_granted = True

if bonus_granted:
    price -= bonus

print("wersja długa:", price)

price = 123
bonus = 23
bonus_granted = True

price = price - bonus if bonus_granted else price
print("Wersja uproszczona:", price)

print()
print()
print()
"""
Zapisz poniższe polecenie if w postaci uproszczonej:
"""

rating = 5

if rating == 5:
    print("wersja długa: very good")
elif rating == 4:
    print("wersja długa: good")
else:
    print("wersja długa: weak")

rate = "very good" if rating is 5 else "good" if rating is 4 else "weak"
print("wersja uproszczona:", rate)
print()
print()
print()
"""
Ktoś był kiedyś niezadowolony, bo w kursie jest za mało polskich akcentów, więc... posłuchaj piosenki De Mono - Niedziela będzie dla nas - https://www.youtube.com/watch?v=lmn0Qf1_eI4 (możesz też skorzystać z oryginalnej wersji: Niebiesko Czarnych: https://www.youtube.com/watch?v=Fxkhe8GqYkc)

Napisz program, który:

zapisze w zmiennej today_weekday nazwę dzisiejszego dnia tygodnia

bazując na pierwszej zwrotce piosenki serią poleceń if/elif/.../else ustali co dzisiaj powinieneś robić

Przepisz powyższy program stosując składnie uproszczona polecenia if

"""

day = datetime.datetime.today().weekday()

if day == 0:
    print("Poniedzialek: ja nie moge bo pomagam mamie")
elif day == 1:
    print("Wtorek: masz w domu pranie")
elif day == 2:
    print("Środa: masz w domu pranie")
elif day == 3:
    print("Czwartek: mam dyżur")
elif day == 4:
    print("Piątek: mam dwa zebrania")
elif day == 5:
    print("Sobota: na lekcje ganiasz")
else:
    print("Niedziela: jest dla nas")


toDo = "Poniedzialek: ja nie moge bo pomagam mamie" if day == 0 else "Wtorek: masz w domu pranie" if day == 1 else "Środa: masz w domu pranie" if day == 2 else "Czwartek: mam dyżur" if day == 3 else "Piątek: mam dwa zebrania" if day == 4 else "Sobota: na lekcje ganiasz" if day == 5 else "Niedziela: jest dla nas"


print("Wersja skrócona:", toDo)

print()
print("##### Wersja instruktora #####")
print()

today_weekday = dt.date.today().strftime("%A")

if today_weekday == 'Monday':
    print("I'm helping my mum")
elif today_weekday == 'Tuesday' or today_weekday == 'Wednesday':
    print("You are doing laundry")
elif today_weekday == 'Thursday':
    print("I'm on duty")
elif today_weekday == 'Friday':
    print("I have two meetings")
elif today_weekday == 'Saturday':
    print("You have lessons")
else:
    print("SUNDAY WILL BE FOR US")


print("I'm helping my mum" if today_weekday == 'Monday' else
      "You are doing laundry" if today_weekday == 'Tuesday' or today_weekday == 'Wednesday' else
      "I'm on duty" if today_weekday == 'Thursday' else
      "I have two meetings" if today_weekday == 'Friday' else
      "You have lessons" if today_weekday == 'Saturday' else
      "SUNDAY WILL BE FOR US")
