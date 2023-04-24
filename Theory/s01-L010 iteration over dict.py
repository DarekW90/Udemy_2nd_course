workDays = [19, 21, 22, 21, 20, 22]
months = ['I', 'II', 'III', 'IV', 'V', 'VI']

monthDays = dict(zip(months, workDays))
print(monthDays)

# for key, value in monthDays:
    # print('Keys is', key, 'value is', value)


for key in monthDays:
    print('Keys is', key, 'value is', monthDays[key])

for value in monthDays.values():
    print('the value is', value)

